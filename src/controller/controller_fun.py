import mysql.connector as conn #import connector module from mysql as conn 

def create_server_connection(host_name, user_name, user_password):
    """
    connect this jupyter with the database. 
    """
    connection = None
    try:
        connection = conn.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_query(connection, query):
    """
    
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    """
    returns list of tuple of each row in the table
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
        
def showDatabasesInSchemas(Schemas_name):
    """
    show the databases within Schemas_name
    """
    cursor=Schemas_name.cursor()
    cursor.execute("show databases")
    print(cursor.fetchall())

def execute_list_query(connection, sql, val):
    """
    assign value in table from val list
    """
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    
"""
..........................................................................................................
"""
    

def createSample(numberOFsamples):
    """
    returns a,b
    where a is the code of the fabric 
      and b is the type of defect 
    """
    
    import time
    import random
    import string
    NN = ""
     
    for i in range(numberOFsamples):
        NN = ''.join(random.choice(string.ascii_letters) for x in range(5))
        for j in range(random.randint(10,15)):
            n = random.randint(1,4)   
            yield NN,n
            time.sleep(1)
        time.sleep(15)
