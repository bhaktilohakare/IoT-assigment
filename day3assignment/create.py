import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# create a query
empid = int(input("Enter empid : "))
name = input("Enter name : ")
department = input("Enter department : ")
email = input("Enter email :")
salary = input("Enter salary : ")
date_of_joining = input("Enter date_of_joining :")

query = f"insert into company values({empid}, '{name}', '1{department}', '{email}', '{salary}','{date_of_joining}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()



