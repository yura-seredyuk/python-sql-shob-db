from conf.connector import Connector


connection, cursor = Connector.openDB()

# query = """INSERT INTO product_category (id,category_name)
#         VALUES
#         (1,'Cheese'),
#         (2,'Fruits'),
#         (3,'Meat'),
#         (4,'Fish'),
#         (5,'Drink');"""
# cursor.execute(query)
# connection.commit()

query = """INSERT INTO country (id, country_name)
            VALUES
            (1,'England'),
            (2,'France'),
            (3,'Spain');"""
cursor.execute(query)
connection.commit()

query = """INSERT INTO city(id, city_name, country_id)
            VALUES
            (1,'London',1),
            (2,'Paris',3),
            (3,'Madrid',2);"""
cursor.execute(query)
connection.commit()

query = """INSERT INTO employee (id, first_name, last_name, date_of_birth, city_id, chief_id)
            VALUES
            (1,'Rahul','Lott','1964-03-23',1,9),
            (2,'Ishaan','Dunn','1972-03-31',1,3),
            (3,'Nina','Palacios','1972-07-26',2,1),
            (4,'Zac','Copeland','1986-08-04',2,1),
            (5,'Stuart','Willis','1993-08-16',3,2),
            (6,'Cristina','Salt','1965-08-31',3,2),
            (7,'Dean' ,'Taylor','1987-02-11',3,3),
            (8,'Joseff','Witt','1995-02-28',2,4),
            (9,'Nathanael','Bartlett','1978-08-29',1,NULL),
            (10,'Zak','Spooner','1997-12-11',2,2);"""
cursor.execute(query)
connection.commit()

query = """INSERT INTO customer (id, city_id, first_name, last_name, date_of_birth)
            VALUES
            (1,2,'Eduard','Alcock','2020-01-25'),
            (2,1,'Yousef','Espinoza','2020-01-25'),
            (3,1,'Luther','Mackie','2020-01-25'),
            (4,3,'Igor','Gunn','2020-01-25'),
            (5,2,'Stacy','Major','2020-01-25'),
            (6,2,'Muhamed','Mustafa','2020-01-25'),
            (7,3,'Harvie' ,'Berry','2020-01-25'),
            (8,1,'Chester','Larson','2020-01-25'),
            (9,2,'Veronika','Regan','2020-01-25'),
            (10,3,'Maddison','Holding','2020-01-25');"""
cursor.execute(query)
connection.commit()

query = """INSERT INTO product (id ,product_name,unit_price,country_id,product_category_id)
            VALUES
            (1,'Tofu',100,2,1),
            (2,'Apple',50,1,2),
            (3,'Meat',150,3,3),
            (4,'Fish',80, 1,4),
            (5,'Coffe',200,3,5),
            (6,'Tea',120,2,5);"""
cursor.execute(query)
connection.commit()

query = """INSERT INTO orders (id,employee_id,customer_id,city_id,date_of_order,product_id,price)
            VALUES
            (1,3,1,2,'2020-01-25',2,700),
            (2,2,2,1,'2020-03-30',2,750),
            (3,4,4,1,'2020-09-03',1,170),
            (4,2,3,3,'2020-11-18',5,100),
            (5,4,5,3,'2020-12-28',4,80),
            (6,5,2,2,'2020-09-07',3,200),
            (7,6,3,1,'2020-11-12',2,800),
            (8,1,5,3,'2020-11-19',1,150),
            (9,2,6,1,'2020-06-12',4,85),
            (10,8,1,3,'2020-07-28',5,100);"""
cursor.execute(query)
connection.commit()

Connector.closeDB(connection, cursor)

