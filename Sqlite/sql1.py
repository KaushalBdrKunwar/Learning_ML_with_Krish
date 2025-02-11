import sqlite3

#Connect to an SQlite database
connection = sqlite3.connect('example.db')
connection

#Cursor
cursor = connection.cursor()

#Create a table
cursor.execute('''
Create Table if Not Exists employees(
            id Integer Primary Key,
            name Text Not Null,
            age  Integer,
            department Text
            )
''')

#Commit the changes
connection.commit()

#Select the element in table
cursor.execute('''
Select * from employees       

''')

cursor.execute("DELETE FROM employees")

# Insert the data into the table
cursor.execute('''
Insert Into employees(name,age,department)
VALUES('Krish',24,'Data Science')
''')

cursor.execute('''
Insert Into employees(name,age,department)
VALUES('John',34,'Data Analyst')
''')

cursor.execute('''
Insert Into employees(name,age,department)
VALUES('Harry',42,'SEO')
''')

#Commit the changes
connection.commit()

#Query the data from the table
cursor.execute('Select * from employees')
rows=cursor.fetchall()

#Print the queried data

for row in rows:
    print(row)

#Update the data in the table
cursor.execute('''
Update employees
Set age=54
Where name="Krish"   
''')

connection.commit()

#Select
cursor.execute('Select * from employees')
records = cursor.fetchall()

for record in records:
    print(record)

# Delete the data from the table
cursor.execute('''
Delete From employees
Where name = 'Harry'
''')
connection.commit()

#Select or Read
cursor.execute('Select * from  employees')
records = cursor.fetchall()

#Print
for record in records:
    print(record)