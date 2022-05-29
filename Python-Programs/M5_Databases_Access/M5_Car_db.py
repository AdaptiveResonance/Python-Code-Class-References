import sqlite3 as sql

conn = sql.connect("cars.db")
print("DB Connection created successfully")

cur = conn.cursor()

cur.execute("Drop table if exists car")

#Create Statement
cur.execute("""CREATE TABLE car(
               ID INTEGER Primary Key AUTOINCREMENT,
               make TEXT not null,
               model TEXT not null,
               manufacture_year int not null,
               price int not null
            )""")
print("Table Created")

cur.execute("""Insert into car(make,model,manufacture_year,price)
            values ('Hyundai','Verna',2020,20000),
            ('Hyundai','Elantra',2021,20000),
            ('BMW','X55',2021,50000),
            ('Audi','Q90',2015,10000),
            ('Toyota','Corolla',2019,15000)""")
print("Data Inserted")

res = cur.execute("Select * from car")
for r in res:
    print(r)

cur.execute("""Update car set price = ( 100 + ? ) * price / 100""",[10])
print("Data Updated")

res = cur.execute("Select * from car")
for r in res:
    print(r)

conn.commit()

conn.close()

