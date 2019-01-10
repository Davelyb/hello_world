# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from mySpider.utils import code_help as ch


class MyspiderPipeline(object):

    def process_item(self, item, spider):
        measurement = ch.get_measurement_by_city_name(item.get('city'))
        data_json = {
            'time': int(time.time()),
            'measurement': measurement,
            'fields': item
        }
        print('*'*50)
        print(data_json)
        # 写入influxdb数据库
        ch.influx.write_points([data_json])
        return item

    def close_spider(self, spider):
        print('close spider...~_~')
