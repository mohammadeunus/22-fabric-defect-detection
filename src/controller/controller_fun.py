import src.model.model_fun as mdl
import src.db.database as db

myDb = db.create_server_connection("localhost", "root", "root")


def sample_create(sample_number):
    for i in mdl.create_sample(sample_number):
        if i[1] == 1:
            sql = "update fabric set hole1=hole1+1 WHERE fabric_id= ({})".format((str(i[0])))
            db.execute_query(myDb, sql)
        elif i[1] == 2:
            sql = "update fabric set NeedleMark2=NeedleMark2+1 WHERE fabric_id= ({})".format((str(i[0])))
            val = (i[0],)
            db.execute_list_query(myDb, sql, val)
        elif i[1] == 3:
            sql = "update fabric set joint3=joint3+1 WHERE fabric_id= ({})".format((str(i[0])))
            val = (i[0],)
            db.execute_list_query(myDb, sql, val)
        elif i[1] == 4:
            sql = "update fabric set penMark4=penMark4+1 WHERE fabric_id= ({})".format((str(i[0])))
            val = (i[0],)
            db.execute_list_query(myDb, sql, val)
