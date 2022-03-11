import src.model.model_fun as mdl
import src.controller.controller_fun as ctr
import src.db.database as db

import mysql.connector as conn  # import a module from mysql

# connected this program with database
myDb = db.create_server_connection("localhost", "root", "root")

# how the databases within myDb
db.show_databases_in_schemas(myDb)

# insert into database based on the return values from the model
for m in mdl.create_sample(5):
    ctr.sample_making(m[0], m[1])
