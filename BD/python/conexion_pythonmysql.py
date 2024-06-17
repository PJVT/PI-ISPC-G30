import mysql.connector

HOST = "localhost"
USER = "root"#
PASSWORD = "password"#
BD = "instituto"#instituto

mydb = mysql.connector.connect(
  host="localhost",user=USER,
  password=PASSWORD,database=BD
)
