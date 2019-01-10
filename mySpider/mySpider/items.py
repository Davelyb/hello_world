# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    current_tem = scrapy.Field()
    humidity = scrapy.Field()
    wind_direct = scrapy.Field()
    wind_level = scrapy.Field()
    pm25 = scrapy.Field()
    
    tem_7d0 = scrapy.Field()
    tem_7d1 = scrapy.Field()
    tem_7d2 = scrapy.Field()
    tem_7d3 = scrapy.Field()
    tem_7d4 = scrapy.Field()
    tem_7d5 = scrapy.Field()
    tem_7d6 = scrapy.Field()

