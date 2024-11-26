# -*- coding: utf-8 -*-
import scrapy, random, os, json
from socFundScraper.items import socFundItem, formdata
from urllib.parse import urlencode
from main import keywords
from fake_useragent import UserAgent

class socFundSpider(scrapy.Spider):

    name = 'socFund'  # 爬虫名称
    allowed_domains = ['fz.people.com.cn']
    # start_urls = ['http://fz.people.com.cn/skygb/sk/index.php/Index/seach']
    
    # 指定检索关键词
    keywords = keywords

    # POST提交参数
    formdata = formdata

    # 参数提交的url
    url = "http://fz.people.com.cn/skygb/sk/index.php/Index/seach"

    state_file = 'job_info.json'
    current_state = None

    def headers(self):
        """
        随机获取身份
        """
        return {'User-Agent': UserAgent().random}
    def save_job_state(self):
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(self.current_state, f, ensure_ascii=False, indent=4)

    def load_job_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'index': 0, 'page': 1}  # Default state

    def start_requests(self):
        """
        POST请求实现一般是重写start_requests函数，指定第一个关键词为默认检索关键词
        :return:
        """
        self.current_state = self.load_job_state()
        self.formdata['xmname'] = self.keywords[self.current_state['index']]
        request_url = self.get_request_url(self.current_state['page'])
        print("关键词：{}即将爬取第{}页数据".format(formdata['xmname'], self.current_state['page']))
        yield scrapy.Request(url=request_url, headers=self.headers(), callback=self.parse, meta={'formdata': self.formdata})

    def get_request_url(self, page):
        """Generate the request URL by appending the page number if it’s greater than 1."""
        if page > 1:
            return f"{self.url}/{page}?{urlencode(self.formdata)}"
        return f"{self.url}?{urlencode(self.formdata)}"

    def parse(self, response):
        """
        解析数据
        :param response:
        :return:
        """
        if response.meta['formdata']:
            self.formdata = response.meta['formdata']

        # 每行数据所在节点
        try:
            node_list = response.xpath("//div[@class='jc_a']/table/*")[1:]
        except:
            print("关键词‘{}’无搜索结果!".format(formdata['xmname']))
        for node in node_list:
            # 提取数据
            item = socFundItem()
            # 关键词
            item['keyword'] = formdata['xmname']
            # 项目编号
            item['pronums'] = node.xpath('./td[1]/span/text()').extract_first()
            # 项目类别
            item['protype'] = node.xpath('./td[2]/span/text()').extract_first()
            # 学科类别
            item['subtype'] = node.xpath('./td[3]/span/text()').extract_first()
            # 项目名称
            item['proname'] = node.xpath('./td[4]/span/text()').extract_first()
            # 立项时间
            item['protime'] = node.xpath('./td[5]/span/text()').extract_first()
            # 负责人
            item['leaders'] = node.xpath('./td[6]/span/text()').extract_first()
            # 工作单位
            item['workloc'] = node.xpath('./td[8]/span/text()').extract_first()
            # 单位类别
            item['orgtype'] = node.xpath('./td[9]/span/text()').extract_first()
            # 所属省市
            item['provloc'] = node.xpath('./td[10]/span/text()').extract_first()
            # 所属系统
            item['systloc'] = node.xpath('./td[11]/span/text()').extract_first()
            # 成果名称
            item['result']= node.xpath('./td[12]/span/text()').extract_first()
            # 成果形式
            item['resulttype'] = node.xpath('./td[13]/span/text()').extract_first()
            # 成果等级
            item['resultlevel'] = node.xpath('./td[14]/span/text()').extract_first()
            yield item

        # 匹配下一页的数据
        next_page = response.xpath("//div[@class='page clear']/a[contains(text(), '下一页')]/@href").get()
        if next_page:
            self.current_state['page'] += 1
            self.save_job_state()
            next_url = self.get_request_url(self.current_state['page'])
            print("关键词：{}即将爬取第{}页数据".format(formdata['xmname'], self.current_state['page']))
            yield scrapy.Request(url=next_url, headers=self.headers(), callback=self.parse, meta={'formdata': response.meta['formdata']})
        else:
            print("关键词：{}的数据爬取完毕，共{}页数据".format(formdata['xmname'], self.current_state['page']))
            self.current_state['index'] += 1
            self.current_state['page'] = 1
            try:
                if response.meta['formdata']:
                    self.formdata = response.meta['formdata']
                self.formdata['xmname'] = self.keywords[self.current_state['index']]
                next_url = self.get_request_url(self.current_state['page'])
                self.save_job_state()
                print("关键词：{}即将爬取第{}页数据".format(formdata['xmname'], self.current_state['page']))
                yield scrapy.Request(url=next_url, headers=self.headers(), callback=self.parse, meta={'formdata': response.meta['formdata']})
            except:
                print("已爬取所有关键词数据")