import src.model.model_fun as mdl
import src.controller.controller_fun as ctr
import src.db.database as db

import mysql.connector as conn  # import a module from mysql

# connected this program with database
myDb = db.create_server_connection("localhost","root","root")

# how the databases within myDb
db.showDatabasesInSchemas(myDb)

def
for i in mdl.createSample(5):
    if i[1] == 1:
        spl = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
        sql = "INSERT INTO  fabric(operation_date, fabric_id, defect_time, hole1) VALUES (%s, %s, %s)"
        val = (i[0], i[1], i[2])
        db.execute_query(myDb, sql, val)
    elif i[1] == 2:
        sql = "INSERT INTO  fabric(operation_date, fabric_id, defect_time, NeedleMark2) VALUES (%s, %s, %s)"
        val = (i[0], i[1], i[2])
        db.execute_query(myDb, sql, val)
    elif i[1] == 3:
        sql = "INSERT INTO  fabric(operation_date, fabric_id, defect_time, joint3) VALUES (%s, %s, %s)"
        val = (i[0], i[1], i[2])
        db.execute_query(myDb, sql, val)
    elif i[1] == 4:
        sql = "INSERT INTO  fabric(operation_date, fabric_id, defect_time, penMark4) VALUES (%s, %s, %s)"
        val = (i[0], i[1], i[2])
        db.execute_query(myDb, sql, val)


def update_url_hits(url,defect_id):
    sql_query = "update fabric set hole1=hole1+1 WHERE fabric_id= %s"
    db.execute_query(myDb, sql_query)

update_url_hits("hole1",1)
