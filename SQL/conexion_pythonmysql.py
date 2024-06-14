import mysql.connector

HOST = "localhost"
USER = "root"#
PASSWORD = "password"#
BD = "instituto"#instituto

mydb = mysql.connector.connect(
  host="localhost",user=USER,
  password=PASSWORD,database=BD
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Persona WHERE id=3")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)