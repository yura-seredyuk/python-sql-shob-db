from conf.connector import Connector


connection, cursor = Connector.openDB()

#
print('\tTASK 2:') 
query = """select count(id) as "Count" from employee where city_id = 1"""
cursor.execute(query)
rezults = cursor.fetchone()
print("Count:",rezults[0])
# 
print('\tTASK 3:')
query = """select  first_name, last_name, date_of_birth
            from employee
            where date_of_birth  in (
            select MIN(date_of_birth) 
            from employee e
            group by city_id)"""
cursor.execute(query)
rezults = cursor.fetchall()
for row in rezults:
    for item in row:
        print(item, end=' ')
    else:
        print()
# 
print('\tTASK 4:')
query = """select  first_name, last_name, date_of_birth
            from employee
            where extract(month from date_of_birth) = extract(month from now())"""
cursor.execute(query)
rezults = cursor.fetchall()
for row in rezults:
    for item in row:
        print(item, end=' ')
    else:
        print()
# 
print('\tTASK 5:')
query = """select  e.first_name,e.last_name from employee e
            where  e.id in(
            select o.employee_id from orders o 
            where o.city_id in(
            select  c.id from  city c where c.city_name = 'Madrid'));"""
cursor.execute(query)
rezults = cursor.fetchall()
for row in rezults:
    for item in row:
        print(item, end=' ')
    else:
        print()
# 
print('\tTASK 6:')
query = """select  e.first_name,e.last_name, count(o.date_of_order) from employee e
            left join orders o on e.id = o.employee_id 
            where extract(year from o.date_of_order) = 2020 and o.date_of_order >'2020-09-03'
            group  by e.first_name, e.last_name;"""
cursor.execute(query)
rezults = cursor.fetchall()
for row in rezults:
    for item in row:
        print(item, end=' ')
    else:
        print()     
# 
print('\tTASK 7:')
query = """select  c.first_name, c.last_name, count(product_id) as "Count", sum(price) as "Sum" from customer c 
            left join orders o on o.customer_id = c.id
            where o.customer_id in(
            select o2.customer_id from orders o2 where o2.product_id in (
            select p.id from product p where p.product_name = 'Tofu'))
            group  by c.first_name, c.last_name,  c.id;"""
cursor.execute(query)
rezults = cursor.fetchall()
for row in rezults:
    for item in row:
        print(item, end=' ')
    else:
        print()   
  
Connector.closeDB(connection, cursor)
