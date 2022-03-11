import src.model.model_fun as mdl
import src.db.database as db

myDb = db.create_server_connection("localhost", "root", "root")


def sample_create(idd: int, effect_no: int):
    """
    takes in fabric_id as idd and effect_no
    and increments the value in of effect_no in idd row
    """
    sql = f"""
    INSERT INTO testy (id, effect1, effect2, effect3)
    SELECT id, (n = 1), (n = 2), (n = 3) FROM (SELECT {idd} id, {effect_no} n) t
    ON DUPLICATE KEY UPDATE effect1 = effect1 + 1, 
                            effect2 = effect2 + 1, 
                            effect3 = effect3 + 1;
    """
    db.execute_query(myDb, sql)


def sample_making(idd: int, effect_no: int):
    """
    takes in fabric_id as idd and effect_no
    and increments the value in of effect_no in idd row
    """
    sql = f"""
    INSERT INTO testy (id, effect{effect_no}) VALUES ({idd}, 1)
    ON DUPLICATE KEY UPDATE effect{effect_no} = effect{effect_no} + 1
    """
    db.execute_query(myDb, sql)
