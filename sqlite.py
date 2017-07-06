import sqlite3
from shgysk8zer0.pyutils.preparedstatement import PreparedStatement

class Sqlite(sqlite3.Connection):
    def __init__(self, db_src: str = ':memory:', *args, **kwargs):
        super().__init__(db_src, *args, **kwargs)
        self.row_factory = lambda c, r: dict([(col[0], r[i]) for i, col in enumerate(c.description)])

    def prepare(self, sql: str) -> PreparedStatement:
        return PreparedStatement(self, sql)

    def select(self, table: str, *args, **kwargs) -> sqlite3.Cursor:
        if len(args) > 0:
            cols = self.__format_cols(args)
        else:
            cols = ['*']

        if len(kwargs) > 0:
            bindings = self.__format_bindings(kwargs.keys())
            sql = 'SELECT {} FROM `{}` WHERE {};'.format(', '.join(cols), table, ' AND '.join(bindings))
        else:
            sql = 'SELECT {} FROM `{}`;'.format(', '.join(cols), table)

        return self.cursor().execute(sql, kwargs)

    def insert(self, table, **kwargs):
        cols = self.__format_cols(kwargs.keys())
        bindings = self.__format_bindings(kwargs.keys())
        sql = 'INSERT INTO `{}` ({}) VALUES ({});'.format(table, ', '.join(cols), ', '.join(bindings))
        return self.execute(sql, kwargs)

    def __format_cols(self, cols: tuple) -> list:
        return ['`{}`'.format(key) for key in cols]

    def __format_bindings(self, cols: tuple) -> list:
        return [':{}'.format(key) for key in cols]
