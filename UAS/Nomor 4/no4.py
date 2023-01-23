import mysql.connector

phpmysql = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "",
    database = "",
)

if phpmysql.is_connected():
    print("Sudah Terkonek")
