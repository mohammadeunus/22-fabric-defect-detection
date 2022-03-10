import src.model.model_fun as mdl
import src.controller.controller_fun as ctr
import src.db.database as db

import mysql.connector as conn  # import a module from mysql

# connected this program with database
myDb = db.create_server_connection("localhost", "root", "root")

# how the databases within myDb
db.show_databases_in_schemas(myDb)

# create samples and upload in database
ctr.sample_create(5)

# def update_url_hits(url, defect_id):
#    sql_query = "update fabric set hole1=hole1+1 WHERE fabric_id= %s"
#    db.execute_query(myDb, sql_query)
#
# update_url_hits("hole1", 1)
