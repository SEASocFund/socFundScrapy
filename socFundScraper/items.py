# -*- coding: utf-8 -*-
# borrowed from https://github.com/z6833/ProSearch
import scrapy

class socFundItem(scrapy.Item):

    # 关键词
    keyword = scrapy.Field()
    # 项目编号
    pronums = scrapy.Field()
    # 项目类别
    protype = scrapy.Field()
    # 学科类别
    subtype = scrapy.Field()
    # 项目名称
    proname = scrapy.Field()
    # 立项时间
    protime = scrapy.Field()
    # 负责人
    leaders = scrapy.Field()
    # 工作单位
    workloc = scrapy.Field()
    # 单位类别
    orgtype = scrapy.Field()
    # 所在省市
    provloc = scrapy.Field()
    # 所属系统
    systloc = scrapy.Field()
    # 成果名称
    result = scrapy.Field()
    # 成果形式
    resulttype = scrapy.Field()
    # 成果等级
    resultlevel = scrapy.Field()

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
