import mysql.connector as conn  # import connector module from mysql as conn


def create_server_connection(host_name, user_name, user_password):
    """
    connect this jupyter notebook with the database.
    """
    connection = None
    try:
        connection = conn.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        cursor = connection.cursor()
        cursor.execute("use mubintest")
        connection.commit()

        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error in create_server_connection: '{err}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("execute_query successful")
    except Exception as err:
        print(f"Error in execute_query: '{err}'")


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
    except Exception as err:
        print(f"Error in read_query: '{err}'")


def show_databases_in_schemas(schemas_name):
    """
    show the databases within Schemas_name
    """
    cursor = schemas_name.cursor()
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
    except Exception as err:
        print(f"Error in execute_list_query: '{err}'")
