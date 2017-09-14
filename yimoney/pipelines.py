# -*- coding: utf-8 -*-

import json

class YimoneyPipeline(object):
    def __init__(self):
        self.f = open("data.josn", "w", encoding="UTF-8")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(json_str + ",\r\n")
        return item

    def close_spider(self, spider):
        self.f.close()