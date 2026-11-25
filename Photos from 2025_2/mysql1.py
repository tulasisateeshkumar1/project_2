import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="sateesh",passwd="2181", database="sateesh")

mycursor=mydb.cursor()
mycursor.execute("select * from employee")
for row in mycursor:
    print(row)