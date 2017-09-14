# -*- coding: utf-8 -*-
import scrapy
import json

from yimoney.items import YimoneyItem

class YimongyAccountSpider(scrapy.Spider):
    name = 'yimongy_account'
    allowed_domains = ['quotes.money.163.com']

    page = 0
    account_url = 'http://quotes.money.163.com/hs/marketdata/service/cwsd.php?host=/hs/marketdata/service/cwsd.php&page=' \
                  + str(page) + \
                  '&query=date:2017-06-30&fields=NO,SYMBOL,SNAME,PUBLISHDATE,MFRATIO28,MFRATIO18,MFRATIO20,MFRATIO10,MFRATIO4,MFRATIO2,MFRATIO12,MFRATIO23,MFRATIO25,MFRATIO24,MFRATIO122&sort=MFRATIO28&order=desc&count=25&type=query&initData=[object%20Object]&callback=callback_1488472914&req=31556'
    start_urls = [account_url]

    def parse(self, response):
        data_dict = response.body[20:-1].decode('UTF-8')
        list = dict(json.loads(data_dict))['list']
        if(len(list) == 0):
            return
        for one in list:
            item = YimoneyItem()

            item['symbol'] = one['SYMBOL']
            item['sname'] = one['SNAME']
            item['publishdate'] = one['PUBLISHDATE']

            if 'MFRATIO28' in one:
                item['income_one'] = one['MFRATIO28']
            else:
                item['income_one'] = ''

            if 'MFRATIO18' in one:
                item['income_one_clean'] = one['MFRATIO18']
            else:
                item['income_one_clean'] = ''

            if 'MFRATIO20' in one:
                item['cash_one'] = one['MFRATIO20']
            else:
                item['cash_one'] = ''

            item['income_main'] = one['MFRATIO10']
            if 'MFRATIO10' in one:
                item['income_main'] = one['MFRATIO10']
            else:
                item['income_main'] = ''

            item['profit_main'] = one['MFRATIO4']
            if 'MFRATIO4' in one:
                item['profit_main'] = one['MFRATIO4']
            else:
                item['profit_main'] = ''

            item['profit_clean'] = one['MFRATIO2']
            if 'MFRATIO2' in one:
                item['profit_clean'] = one['MFRATIO2']
            else:
                item['profit_clean'] = ''

            item['property_all'] = one['MFRATIO12']
            if 'MFRATIO12' in one:
                item['property_all'] = one['MFRATIO12']
            else:
                item['property_all'] = ''

            item['property_flow'] = one['MFRATIO23']
            if 'MFRATIO23' in one:
                item['property_flow'] = one['MFRATIO23']
            else:
                item['property_flow'] = ''

            item['debt_all'] = one['MFRATIO25']
            if 'MFRATIO25' in one:
                item['debt_all'] = one['MFRATIO25']
            else:
                item['debt_all'] = ''

            item['debt_flow'] = one['MFRATIO24']
            if 'MFRATIO24' in one:
                item['debt_flow'] = one['MFRATIO24']
            else:
                item['debt_flow'] = ''

            item['property_clean'] = one['MFRATIO122']
            if 'MFRATIO122' in one:
                item['property_clean'] = one['MFRATIO122']
            else:
                item['property_clean'] = ''

            yield item

        self.page += 1
        url = account_url = 'http://quotes.money.163.com/hs/marketdata/service/cwsd.php?host=/hs/marketdata/service/cwsd.php&page=' \
                  + str(self.page) + \
                  '&query=date:2017-06-30&fields=NO,SYMBOL,SNAME,PUBLISHDATE,MFRATIO28,MFRATIO18,MFRATIO20,MFRATIO10,MFRATIO4,MFRATIO2,MFRATIO12,MFRATIO23,MFRATIO25,MFRATIO24,MFRATIO122&sort=MFRATIO28&order=desc&count=25&type=query&initData=[object%20Object]&callback=callback_1488472914&req=31556'
        yield scrapy.Request(url, callback=self.parse)
