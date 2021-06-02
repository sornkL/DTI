import pymysql

from typing import *

from Settings import *


class ConnectionTool:
    def __init__(self):
        self._db = None
        self._cursor = None

    def _connect_database(self) -> None:
        self._db = pymysql.connect(HOST, USER_NAME, USER_PASSWORD, DATABASE_NAME)
        self._cursor = self._db.cursor()

    def select(self, sql: str) -> tuple:
        try:
            self._connect_database()
            self._cursor.execute(sql)
        except Exception as errorMessage:
            print(errorMessage)
        finally:
            self._db.close()

        return self._cursor.fetchall()

    def select_one_result(self, sql: str) -> Any:
        try:
            self._connect_database()
            self._cursor.execute(sql)
        except Exception as errorMessage:
            print(errorMessage)
        finally:
            self._db.close()

        return self._cursor.fetchone()

    def insert(self, sql: str) -> None:
        pass

    def update(self, sql: str) -> None:
        pass


if __name__ == '__main__':
    connectionTool = ConnectionTool()

    sqlForTestOne = "select count(*) from tblBindingDemo"
    sqlForTestAll = "select * from tblTest"

    print(connectionTool.select_one_result(sqlForTestOne))
    print(connectionTool.select(sqlForTestAll))
