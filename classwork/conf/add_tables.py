import psycopg2
from .settings import *


def create_tables(db_name = None):
    if db_name is None:
        db_name = DB_NAME
    connection = psycopg2.connect(user = USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT,
                                database = db_name)


    cursor = connection.cursor()
    country = """CREATE TABLE IF NOT EXISTS country(
                id SERIAL PRIMARY KEY,
                country_name varchar(50) NOT NULL)"""
    cursor.execute(country)
    connection.commit()

    city = """CREATE TABLE IF NOT EXISTS city(
                id SERIAL PRIMARY KEY,
                city_name varchar(50) NOT NULL,
                country_id INT REFERENCES country(id))"""
    cursor.execute(city)
    connection.commit()

    employee = """CREATE TABLE IF NOT EXISTS employee(
                id SERIAL PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                date_of_birth DATE NOT NULL,
                city_id INT REFERENCES city(id),
                chief_id INT REFERENCES employee(id))"""
    cursor.execute(employee)
    connection.commit()

    customer = """CREATE TABLE IF NOT EXISTS customer(
                id SERIAL PRIMARY KEY,
                city_id INT REFERENCES city(id),
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                date_of_birth DATE NOT NULL)"""
    cursor.execute(customer)
    connection.commit()

    category = """CREATE TABLE IF NOT EXISTS product_category(
                id SERIAL PRIMARY KEY,
                category_name varchar(50) NOT NULL)"""
    cursor.execute(category)
    connection.commit()

    product = """CREATE TABLE IF NOT EXISTS product(
                id SERIAL PRIMARY KEY,
                product_name varchar(50) NOT NULL,
                unit_price real NOT NULL,
                country_id INT REFERENCES country(id),
                product_category_id INT REFERENCES product_category(id))"""
    cursor.execute(product)
    connection.commit()

    order = """CREATE TABLE IF NOT EXISTS orders(
                id SERIAL PRIMARY KEY,
                employee_id INT REFERENCES employee(id),
                city_id INT REFERENCES city(id),
                date_of_order DATE NOT NULL,
                customer_id INT REFERENCES customer(id),
                product_id INT REFERENCES product(id),
                price real NOT NULL)"""
    cursor.execute(order)
    connection.commit()

    cursor.close()
    connection.close()
