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
