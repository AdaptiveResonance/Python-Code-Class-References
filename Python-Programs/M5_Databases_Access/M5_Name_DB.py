# -*- coding: utf-8 -*-
import sqlite3 as sql

conn = sql.connect("test.db")
print("DB Connection created successfully")

cur = conn.cursor()

#Drop Statement
cur.execute("Drop table if exists student")

#Create Statement
cur.execute("""CREATE TABLE student(
               ID INTEGER Primary Key AUTOINCREMENT,
               NAME TEXT not null,
               AGE INT not null
            )""")
print("Table Created")

#Alter Statement
cur.execute("""Alter Table student rename column name TO student_name""")
print("Table Altered")

#Insert Statement
cur.execute("""Insert into student(student_name,age) 
            values ('Sam',22),('Joel',24),('Kim',21),('Sarah',26)""")
print("Data Inserted")

#Update Statement
cur.execute("""Update student set age=25 where student_name = 'Sarah'""")
print("Data Updated")

#Delete Statement
cur.execute("Delete from student where student_name = 'Joel'")
print("Data Deleted")

#select statement
res = cur.execute("Select * from student")
for r in res:
    print(r)

print("Parameterized Queries")
# Parameterized Update
cur.execute("Update student set age=? where student_name = ?",
            [30,'Kim'])

# Parameterized select
res = cur.execute("Select * from student where student_name = ?",
                  ['Kim'])
for r in res:
    print(r)
conn.commit()

conn.close()

