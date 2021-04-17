import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'DBTEST'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'latin1'". format(DB_NAME))
                    
    print(f"Database {DB_NAME} created!")

def create_tables():
    cursor.execute(f"USE {DB_NAME}")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({})".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists")
            else:
                print(err.msg)

create_database()
create_tables()