#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Goodness_123',

)

#prepare cursor object 
cursorObject = dataBase.cursor()

#creating database
cursorObject.execute("CREATE DATABASE crm_db")

print("All Done!")