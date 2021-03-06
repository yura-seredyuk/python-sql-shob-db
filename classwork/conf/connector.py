import psycopg2
from .settings import *
import sys



class Connector:

    @classmethod
    def dbServerConnection(cls):
        connection = psycopg2.connect(user = USER,
                                    password = PASSWORD,
                                    host = HOST,
                                    port = PORT)
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def dbServerConnectionClose(cls, connection ,cursor):
        cursor.close()
        connection.close()

    @classmethod
    def openDB(cls):
        if 'unittest' in sys.argv[0]:
            db_name = 'test_db'
        else:
            db_name = DB_NAME
        connection = psycopg2.connect(user = USER,
                                    password = PASSWORD,
                                    host = HOST,
                                    port = PORT,
                                    database = db_name)
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def closeDB(cls, connection ,cursor):
        cursor.close()
        connection.close()
        

    def getData(self, table:tuple, fields:tuple, selector=''):
        connection, cursor = self.openDB()
        select_query = f"""
                SELECT  {','.join(fields)} 
                FROM  {','.join(table)} 
                {selector} 
                ORDER BY id;"""
        cursor.execute(select_query)
        rezults = cursor.fetchall()
        self.closeDB(connection, cursor)
        return rezults

    def postData(self, table:str, data:list):
        connection, cursor = self.openDB()
        fields = list(data[0].keys())
        fields.append('id')
        next_id = self.getNextId(table)
        values = ''
        for row in data:
            value = f"""({','.join(map(lambda item: f"'{item}'", row.values()))}, {next_id}),"""
            next_id += 1
            values += value
        insert_query = f"""INSERT INTO {table}
                            ({','.join(fields)})
                            VALUES {values[:-1]}"""
        cursor.execute(insert_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return "Insert done!"

    def updateData(self, table:str, data:dict, selector:str):
        connection, cursor = self.openDB()
        set_items = ''
        for key in data:
            set_items += f"""{key} = '{data[key]}',"""
        update_query = f"""UPDATE {table}
                        SET {set_items[:-1]}
                        WHERE {selector}"""
        cursor.execute(update_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return "Update done!"

    def deleteData(self, table:str, selector:str):
        connection, cursor = self.openDB()
        delete_query = f"""DELETE FROM {table} WHERE {selector}"""
        cursor.execute(delete_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return "Item was deleted!"


    def getNextId(self, table):
        table = (table,)
        fields = ('id',)
        rezult = self.getData(table=table, fields=fields)
        if rezult == []:
            return 1
        return rezult[-1][0] + 1

    def register(self, login, password, role):
        data = [{
            'login': login,
            'password': password,
            'role': role,
        }]
        find_login = self.getData(('reg_base',),('login',),
                    f"WHERE login = '{login}'")
        if not find_login:
            self.postData('reg_base', data=data)
        else:
            print('This login is already exists!')

    def login_check(self, login, password, role):
        find_login = self.getData(('reg_base',),('*',),
                    f"WHERE login = '{login}'")
        if find_login:
            if password == find_login[0][2] and role == find_login[0][3]:
                return find_login[0][0]
            else:
                return False
        else:
            return False
            
