import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CalaClara21",
    port=3307
)

print(mydb)
