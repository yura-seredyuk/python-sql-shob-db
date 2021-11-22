from conf.connector import Connector
import unittest


class AdminFunc(Connector):

    def __init__(self, login, password):
        self.login = login  
        self.password = password
        self.role = 'adm'

    def register_self(self):
        self.register(self.login, self.password, self.role)

    def login_self(self):
        return self.login_check(self.login, self.password, self.role)

    def get_product_category(self, id = None, name = None):
        if self.login_self():
            fields = ('*',)
            table = ('product_category',)
            if id and id.isdigit():
                selector = f"where id = {id}"
            elif name:
                selector = f"where category_name = '{name}'"
            else:
                selector = ""
            return self.getData(table, fields, selector)
        else:
            return "Permission denied! Incorrect login or password."

    def get_product(self, id = None, name = None):
        fields = ('*',)
        table = ('product',)
        if id and id.isdigit():
            selector = f"where id = {id}"
        elif name:
            selector = f"where product_name = '{name}'"
        else:
            selector = ""
        return self.getData(table, fields, selector)
        
    def add_product_category(self, data):
        table = 'product_category'
        return self.postData(table, data)

    def add_product(self, data):
        table = 'product'
        return self.postData(table, data)

    def edit_product_category(self,data):
        table = 'product_category'
        selector = f"""{data["search_field"]} = '{data["search_parameter"]}'"""
        data = data['data']
        return self.updateData(table, data, selector)

    def delete_product_category(self, data):
        table = 'product_category'
        selector = f"""{list(data.keys())[0]} = '{list(data.values())[0]}'"""
        return self.deleteData(table, selector)
 
    def get_order_info(self, category ='', selector=''):
        if self.login_self():
            categoryes = ['city_id', 'date_of_order', 'product_name', 'status']
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name, o.date_of_order, concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price, o.status""",)
            if category and category in categoryes and selector != '':
                where = f"""where {category} = {selector}"""
            else:
                where = ''
            selector = f"""left join employee e on e.id = o.employee_id
                left join city c on c.id = o.city_id 
                left join customer c2 on c2.id = o.customer_id 
                left join product p on p.id = o.product_id 
                {where} """
            rezult = self.getData(table, fields, selector)
            return rezult
        else:
            return "Permission denied! Incorrect login or password."



class AdminTest(unittest.TestCase):
    pass

if __name__ == "__main__":

    admin = AdminFunc(login='admin', 
                    password='admin')  
    # rez = admin.get_product_category(id = '1', name='Fruits')
    # print(rez)

    rez = admin.get_order_info(category ='id', selector='1')
    print(rez)

    # rez = admin.get_product(id = '1', name='Meat')
    # print(rez)

    # post_data = [
    #     {
    #         'category_name': 'Vine',
    #     },
    #     {
    #         'category_name': 'Tea',
    #     },
    # ]
    # post = admin.add_product_category(post_data)
    # print(post)

    # post_data = [
    #     {
    #         'product_name':'Carp',
    #         'unit_price': '80',
    #         'country_id': '1',
    #         'product_category_id': '1',
    #     },
    #     {
    #         'product_name':'Okun',
    #         'unit_price': '40',
    #         'country_id': '1',
    #         'product_category_id': '1',
    #     },
    # ]
    # post = admin.add_product(post_data)
    # print(post)

    # update_data = {
    #     # filter:[(field, parameter,)]
    #     'search_field':'id',
    #     'search_parameter': 8, 
    #     'data':
    #        {   
    #         'category_name': 'Water',
    #        } 
    # }
    # edit = admin.edit_product_category(update_data)
    # print(edit)
         
    # delete = admin.delete_product_category({'id':9})
    # print(delete)