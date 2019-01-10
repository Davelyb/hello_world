# -*- coding: utf-8 -*-
import traceback

from scrapy import Spider, Request
from selenium import webdriver
from mySpider.items import MyspiderItem
from mySpider.utils import code_help as ch


class MySpider(Spider):
    name = "my_spider"

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/Caskroom/chromedriver/2.45/chromedriver')
        # self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        self.browser.close()

    def start_requests(self):
        start_urls = ch.get_all_weather_urls()
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        item = MyspiderItem()
        domain = response.url.split("/")[-2]

        # filename = '%s.html' % domain
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        try:
            if domain == 'weather1d':
                current_tem = response.xpath("//div[@class='tem']/span/text()").extract()
                humidity = response.xpath("//div[@class='zs h']/em/text()").extract()
                wind_direct = response.xpath("//div[@class='zs w']/span/text()").extract()
                wind_level = response.xpath("//div[@class='zs w']/em/text()").extract()

                item['current_tem'] = float(current_tem[0])
                item['humidity'] = float(humidity[0].strip('%'))
                item['wind_direct'] = wind_direct[0]
                item['wind_level'] = float(wind_level[0].strip('级'))

                # print('实时温度:', current_tem)
                # print('相对湿度:', humidity)
            elif domain == 'weather':
                seven_day = response.xpath("//div[@id='7d']/ul[@class='t clearfix']")
                seven_day_lt = []

                for i in range(1, 8):
                    low_temp_lt = seven_day.xpath("li[%s]/p[@class='tem']/span/text()" % str(i)).extract()
                    high_temp_lt = seven_day.xpath("li[%s]/p[@class='tem']/i/text()" % str(i)).extract()
                    # print(low_temp_lt, high_temp_lt)

                    low_temp = low_temp_lt[0] if low_temp_lt else ''
                    high_temp = high_temp_lt[0] if high_temp_lt else ''
                    seven_day_lt.append(low_temp.strip('℃') + '/' + high_temp.strip('℃'))

                for i in range(len(seven_day_lt)):
                    item['tem_7d' + str(i)] = seven_day_lt[i]

            elif domain == 'city':
                pm25 = response.xpath("//div[@class='panel']/b/text()").extract()
                # print('PM2.5:', pm25)
                item['pm25'] = float(pm25[0])
        except:
            print(traceback.format_exc())

        item['city'] = ch.get_city_name_by_url(response.url)
        yield item
