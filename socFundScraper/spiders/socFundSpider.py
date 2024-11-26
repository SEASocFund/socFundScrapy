# -*- coding: utf-8 -*-
import scrapy
from socFundScraper.items import socFundItem
from urllib.parse import urlencode
from main import keywords
from fake_useragent import UserAgent
import random

class socFundSpider(scrapy.Spider):

    name = 'socFund'  # 爬虫名称
    allowed_domains = ['fz.people.com.cn']
    # start_urls = ['http://fz.people.com.cn/skygb/sk/index.php/Index/seach']
    page = 1

    # 指定检索关键词
    keywords = keywords
    # 角标
    index = 0

    # 随机用户代理
    headers= {'User-Agent': UserAgent().random}
    # POST提交参数
    formdata = {
        'pznum': '',
        'xmtype': '0',
        'xktype': '0',
        'xmname': '', # 关键词
        'lxtime': '0', # 立项时间（年份）
        'xmleader': '',
        'zyzw': '0',
        'gzdw': '',
        'dwtype': '0',
        'szdq': '0',
        'ssxt': '0',
        'cgname': '',
        'cgxs': '0',
        'cglevel': '0',
        'jxdata': '0',
        'jxnum': '',
        'cbs': '',
        'cbdate': '0',
        'zz': '',
        'hj': '' 
    }

    # 参数提交的url
    url = "http://fz.people.com.cn/skygb/sk/index.php/Index/seach"

    def start_requests(self):
        """
        POST请求实现一般是重写start_requests函数，指定第一个关键词为默认检索关键词
        :return:
        """
        self.formdata['xmname'] = self.keywords[self.index]
        # self.formdata['lxtime'] = str(self.years)
        # yield scrapy.FormRequest(
        #     url=self.url,
        #     headers=headers,
        #     formdata=self.formdata,
        #     callback=self.parse,
        #     meta={'formdata': self.formdata}
        # )
        request_url = f"{self.url}?{urlencode(self.formdata)}"
        self.log(f"Requesting {request_url}")
        yield scrapy.Request(url=request_url, headers=self.headers, callback=self.parse, meta={'formdata': self.formdata})

    def parse(self, response):
        """
        解析数据
        :param response:
        :return:
        """
        if response.meta['formdata']:
            formdata = response.meta['formdata']

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
            self.page += 1
            print("关键词：{}即将爬取第{}页数据".format(formdata['xmname'], self.page))
            # n_url = self.url + '?' + 'xmname={}&p={}'.format(formdata['xmname'], self.page)
            # yield scrapy.Request(url=n_url, callback=self.parse, meta={'formdata': formdata})
            next_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_url, callback=self.parse, meta={'formdata': response.meta['formdata']})
        else:
            print("关键词：{}的数据爬取完毕，共{}页数据".format(formdata['xmname'], self.page))
            self.index += 1
            try:
                keyword = self.keywords[self.index]
                yield self.start_requests()
            except:
                print("已爬取所有关键词数据")
