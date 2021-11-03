import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from .settings import *


def create():
    connection = psycopg2.connect(user = USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    cursor.execute(f'CREATE DATABASE {DB_NAME}')
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create()