import psycopg2
from .settings import *


class Connector:

    @classmethod
    def openDB(cls):
        connection = psycopg2.connect(user = USER,
                                    password = PASSWORD,
                                    host = HOST,
                                    port = PORT,
                                    database = DB_NAME)
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def closeDB(cls, connection ,cursor):
        cursor.close()
        connection.close()