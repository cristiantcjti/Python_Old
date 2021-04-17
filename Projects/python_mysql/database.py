import mysql.connector

config =  {
    'user': 'root',
    'password': '060390',
    'host': 'localhost',
    'database':'DBTEST'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

