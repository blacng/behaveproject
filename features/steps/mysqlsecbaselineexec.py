import mysql.connector
from mysql.connector import errorcode
from mysql.connector import connection
import databaseconfig as cfg

class MySQLUtils:

    def __init__(self):
        """
        docstring
        """
        pass

    def executemysqlquery(self, query):
        """
        docstring
        """
        connection = mysql.connector.connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

    def shouldnotexist(self, query):
        """
        docstring
        """
        rows = self.executemysqlquery(query)
        return len(rows) == 0

    def variablevalueshouldbe(self, variablename, value):
        """
        docstring
        """
        rows = self.executemysqlquery("SHOW VARIABLES WHERE VARIABLE_NAME = '" + variablename + "'")
        print(rows[0]["Value"])
        return rows[0]["Value"] == value