import src.model.model_fun as mdl
import src.controller.controller_fun as ctr

import mysql.connector as conn  # import a module from mysql

#connected this program with database
myDb = ctr.create_server_connection("localhost","root","root")

#show the databases within myDb
mdl.showDatabasesInSchemas(myDb)

