# -*- coding: utf-8 -*-

import scrapy

class YimoneyItem(scrapy.Item):
    # 股票代码
    symbol = scrapy.Field()
    # 股票名称
    sname = scrapy.Field()
    # 报告日期
    publishdate = scrapy.Field()
    # 基本每股收益
    income_one = scrapy.Field()
    # 每股净资产
    income_one_clean = scrapy.Field()
    # 每股经营现金流
    cash_one = scrapy.Field()
    # 主营业务收入（万元）
    income_main = scrapy.Field()
    # 主营业务利润（万元）
    profit_main = scrapy.Field()
    # 净利润（万元）
    profit_clean = scrapy.Field()
    # 总资产（万元）
    property_all = scrapy.Field()
    # 流动资产（万元）
    property_flow = scrapy.Field()
    # 总负债（万元）
    debt_all = scrapy.Field()
    # 流动负债（万元）
    debt_flow = scrapy.Field()
    # 净资产（万元）
    property_clean = scrapy.Field()

