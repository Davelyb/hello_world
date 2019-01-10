import traceback

from influxdb import InfluxDBClient


__all__ = ["InfluxdbDriver"]


class InfluxdbDriver(InfluxDBClient):

    def __init__(self, host, user, password, port, database):
        super(InfluxdbDriver, self).\
            __init__(host, port, user, password, database, timeout=10)
        # self.database = database

    def write_points(self, data):

        try:
            super(InfluxdbDriver, self).\
                write_points(data, time_precision="s")
            return {"is_success": 1, "error": ""}
        except:
            return {"is_success": 0, "error": traceback.format_exc()}
