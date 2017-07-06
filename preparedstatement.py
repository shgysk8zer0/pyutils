import sqlite3
class PreparedStatement:
    __cursor = None
    __sql = ''
    __params = {}

    def __init__(self, con: sqlite3.Connection, sql: str):
        self.__cursor = con.cursor()
        self.__sql = sql
        self.__params = {}

    def __str__(self) -> str:
        return self.__sql

    def __getitem__(self, key: str):
        return self.__params.get(key)

    def __delitem__(self, key: str):
        del self.__params[key]

    def __contains__(self, key: str) -> bool:
        return key in self.__params

    def __setitem__(self, name: str, value) -> None:
        self.__params[name] = value

    def __call__(self, **kwargs):
        return self.__cursor.execute(self.__sql, {**kwargs, **self.__params})

    def bind(self, name: str, value):
        self.__params[name] = value
        return self

    def bindall(self, **kwargs):
        self.__params = kwargs
        return self

    def execute(self, **kwargs):
        return self._cursor.execute(self.__sql, {**self.__params, **kwargs})

    def executemany(self, *args):
        result = [{**self.__params, **arg} for arg in args]
        return self.__cursor.executemany(self.__sql, result)

    @property
    def params(self) -> dict:
        return self.__params
