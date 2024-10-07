import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "bilal123",
    auth_plugin='mysql_native_password',
    
    )

cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")