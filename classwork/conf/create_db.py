import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from .settings import *


def create(db_name = None):
    connection = psycopg2.connect(user = USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    if db_name is None:
        db_name = DB_NAME
    cursor = connection.cursor()
    cursor.execute(f'CREATE DATABASE {db_name}')
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create()