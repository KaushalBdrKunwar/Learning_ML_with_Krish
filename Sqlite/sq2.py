# Working With the Sales Data
import sqlite3

# Connect to Sqlite
connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

#Create Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER
    region TEXT
)
''')

#Inset data
sales_data = [
    ('2023-01-01','Product1',100,'North'),
    ('2023-01-02','Product2',200,'South'),
    ('2023-01-03','Product3',150,'East'),
    ('2023-01-04','Product4',300,'West'),
    ('2023-01-05','Product5',800,'South')
]

cursor.executemany('''
Insert into sales(date,product,sales,region)
                   values(?,?,?,?)
''',sales_data)

connection.commit()
