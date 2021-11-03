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
Connector.closeDB(connection, cursor)
