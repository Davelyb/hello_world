# coding=utf-8
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import or_


__all__ = ["MysqldbDriver"]


class SqlalchemyDriver(object):

    def __init__(self, host, user, password, port, database):
        db = "mysql+mysqldb://{user}:{password}@{host}:{port}/{database}?"\
            "charset=utf8".format(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
        self.engine = create_engine(db, pool_pre_ping=True)# , echo=True)

    def set_session(self):
        return Session(self.engine, autoflush=True)

    def get_table_classes(self):
        base = automap_base()
        base.prepare(self.engine, reflect=True)
        return base.classes


class MysqldbDriver(object):

    def __init__(self, host, user, password, port, database):
        drv = SqlalchemyDriver(host, user, password, port, database)
        self.session = drv.set_session()
        self.classes = drv.get_table_classes()
        self.kwargs = {"host": host, "user": user, "password": password,
                       "port": port, "database": database}
        self.drv = drv

    def search_cityweather_by_weatherurl(self, url):
        return self.session.query(self.classes.cityweather_cityweather).\
            filter(self.classes.cityweather_cityweather.weather_url.\
                   contains(url)).first()

    def search_measurement_by_city_name(self, city_name):
        return self.session.query(self.classes.cityweather_cityweather).\
            filter_by(city_name=city_name).first()

    def get_cityweathers(self, limit=50):
        cityweather = self.classes.cityweather_cityweather
        session = self.drv.set_session()
        results = session.query(cityweather).limit(limit).all()
        session.close()
        return results

    def add(self, item):
        self.session.add(item)
        self.session.flush()
        self.session.commit()

    def add_all(self, items):
        self.session.add_all(items)
        self.session.flush()
        self.session.commit()

    def commit(self):
        self.session.commit()
