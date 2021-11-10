from conf.connector import Connector


class AdminFunc(Connector):

    def __init__(self, login, password):
        self.login = ''  
        self.password = ''
        self.role = 'adm'      
    
    def get_product_category(self, id = None, name = None):
        fields = ('*',)
        table = ('product_category',)
        if id and id.isdigit():
            selector = f"where id = {id}"
        elif name:
            selector = f"where category_name = '{name}'"
        else:
            selector = ""
        return self.getData(table, fields, selector)

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
 
    

if __name__ == "__main__":

    admin = AdminFunc(login='admin', 
                    password='admin')  

    # rez = admin.get_product_category(id = '1', name='Fruits')
    # print(rez)

    # rez = admin.get_product(id = '1', name='Meat')
    # print(rez)

    post_data = [
        {
            'category_name': 'Vine',
        },
        {
            'category_name': 'Tea',
        },
    ]
    post = admin.add_product_category(post_data)
    print(post)

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