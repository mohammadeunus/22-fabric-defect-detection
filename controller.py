import mysql.connector as conn  # import a module from mysql
import model as mdl

myDb = conn.connect(
    host="localhost",
    user="root",
    passwd="root"
)

cursor = myDb.cursor()


for i in mdl.createSample(5):
    a1, b1 = str(i[0]), int(i[1])

    sql = "INSERT INTO data (address, id) VALUES (%s, %s)"
    val = (a1, b1)

    cursor.execute(sql, val)
    myDb.commit()

    print(cursor.rowcount, "details inserted")

