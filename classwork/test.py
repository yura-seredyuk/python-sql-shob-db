import unittest
from conf.create_db import create as create_db
from conf.add_tables import create_tables
from conf.connector import Connector
from conf.settings import *

from admin import AdminFunc

PRODUCT_DATA = [{
                    'category_name': 'Vine',
                }]
update_data = {
        'search_field':'id',
        'search_parameter': 1, 
        'data':
           {   
            'category_name': 'Water',
           } 
    }

class AdminTest(unittest.TestCase):

    # def setUp(self) -> None:
    @classmethod
    def setUpClass(cls):
        create_db('test_db')
        print('Database "test_db" was created.')
        create_tables('test_db')
        print('All tables created.')

    @classmethod
    def tearDownClass(cls):
        connection, cursor = Connector.dbServerConnection()
        cursor.execute("DROP DATABASE test_db")
        Connector.dbServerConnectionClose(connection, cursor)
        print('Database "test_db" was deleted.')

    def setUp(self) -> None:    
        self.admin = AdminFunc(login='admin', 
                    password='admin')

    # def tearDown(self) -> None:
    #     connection, cursor = Connector.dbServerConnection()
    #     # cursor.execute("DROP DATABASE test_db")
    #     cursor.execute("""DROP DATABASE test_db;""")
    #     Connector.dbServerConnectionClose(connection, cursor)
    #     print('Database "test_db" was deleted.')

    def test_1_post_data(self):
        connection, cursor = Connector.openDB()
        self.admin.add_product_category(PRODUCT_DATA)
        cursor.execute('SELECT * FROM product_category')
        rezults = cursor.fetchall()
        print(rezults)
        self.assertEqual(rezults, [(1, 'Vine')])
        print('Test 1.1 passed')

        self.admin.edit_product_category(update_data)

        cursor.execute('SELECT * FROM product_category')
        rezults = cursor.fetchall()
        print(rezults)
        self.assertEqual(rezults, [(1, 'Water')])
        print('Test 1.2 passed')
        Connector.closeDB(connection, cursor)

    def test_2_edit_data(self):
        connection, cursor = Connector.openDB()
        self.admin.edit_product_category(update_data)

        cursor.execute('SELECT * FROM product_category')
        rezults = cursor.fetchall()
        print(rezults)
        self.assertEqual(rezults, [(1, 'Water')])
        Connector.closeDB(connection, cursor)





