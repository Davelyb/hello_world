from .influxdb_driver import InfluxdbDriver
from .mysqldb_driver import MysqldbDriver
from .local_settings import MYSQLDB_SETTING, INFLUXDB_SETTING

import json


class CodeHelper(object):
    def __init__(self):
        # self.mysql = MysqldbDriver(
        #     host=MYSQLDB_SETTING["host"],
        #     user=MYSQLDB_SETTING["user"],
        #     password=MYSQLDB_SETTING["password"],
        #     port=MYSQLDB_SETTING["port"],
        #     database=MYSQLDB_SETTING["database"]
        # )

        self.influx = InfluxdbDriver(
            host=INFLUXDB_SETTING["host"],
            user=INFLUXDB_SETTING["user"],
            password=INFLUXDB_SETTING["password"],
            port=INFLUXDB_SETTING["port"],
            database=INFLUXDB_SETTING["database"]
        )

    # def get_city_name_by_url(self, url):
    #     city_weather = self.mysql.search_cityweather_by_weatherurl(url)
    #     return city_weather.city_name
    #
    # def get_measurement_by_city_name(self, city_name):
    #     city_weather = self.mysql.search_measurement_by_city_name(city_name)
    #     return city_weather.measurement
    #
    # def get_all_weather_urls(self):
    #     city_weathers = self.mysql.get_cityweathers()
    #     urls = []
    #     for city in city_weathers:
    #         print(city.city_name)
    #         urls.extend(json.loads(city.weather_url))
    #
    #     return urls


code_help = CodeHelper()