import sqlite3
from shgysk8zer0.pyutils.preparedstatement import PreparedStatement

class Sqlite(sqlite3.Connection):
    def __init__(self, db_src: str = ':memory:', *args, **kwargs):
        super().__init__(db_src, *args, **kwargs)
        self.row_factory = lambda c, r: dict([(col[0], r[i]) for i, col in enumerate(c.description)])

    def prepare(self, sql: str) -> PreparedStatement:
        return PreparedStatement(self, sql)
