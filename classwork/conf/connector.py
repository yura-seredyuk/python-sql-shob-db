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
