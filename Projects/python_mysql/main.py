from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print(f"Added log {log_id}")

def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()
    size = len(result)
    
    if size != 0:
        for row in result:
            print(row[0])
    else:
        print("There is no log records!")

def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone() 
    
    if result != None:
        for row in result:
            print(row)
        return row 
    else:
        print(f"There is no log {id} recorded!")

def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log updated :", get_log(id))  


def delete_log(id):
    if get_log(id) != None:
        sql = ("DELETE FROM logs WHERE id = %s")
        cursor.execute(sql, (id,))
        db.commit()
        print("Log deleted")  


#venv deactivate

### Add a log ###
#add_log('It is one more log', 'Jonathan')
#add_log('It is one more log', 'Bruno')
#add_log('It is one more log', 'Cristian')

### Return all logs ###
#get_logs()

### To add an id to return one log ###
#get_log(11) 

### Update a log ###
#update_log(11, "Updated log")

#### Delete one log ###
#delete_log(11)