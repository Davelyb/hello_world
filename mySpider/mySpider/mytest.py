# -*- coding: utf-8 -*-

from mySpider.utils import code_help as ch
import json
import time


def test_mysql():
    # print(mysql.classes.cityweather_cityweather)
    # print(mysql.classes.cityweather_weatherinfo)

    urls = ch.get_all_weather_urls()

    url = 'http://www.86pm25.com/city/suzhou.html'

    print(urls)
    print(ch.get_city_name_by_url(url))
    print(ch.get_measurement_by_city_name('yanqing'))


if __name__ == '__main__':
    pass
    # test_mysql()
    data_json = {
        'time': int(time.time()),
        'measurement': 'TStest2',
        'fields': {
            # 'city_name': 'yanqing',
            # 'current_temp': '-3',
            # 'humility': '35%',
            # 'pm25': '35',
            # 'd1': '-4℃/13℃',
            # 'wind_direct': '西北风'
            'temd2': 40.1,
            'temd3': 30.1,
            'temd4': '0',
            'temd5': '0',
            'temd6': '0',
            'temd7': '0',
        }

    }
    print(ch.influx.write_points([data_json]))