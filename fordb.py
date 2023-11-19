import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("E:\\sm_app.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY,
  user_name TEXT,
  user_surname TEXT,
  email TEXT,
  phone_number INTEGER
);
        """

        execute_query(connection, create_users_table)


create_types_table = """
    CREATE TABLE types (
  type_id INTEGER PRIMARY KEY,
  type_name TEXT,
  type_description TEXT
);
    """

    execute_query(connection, create_types_table)


create_menu_table = """
    CREATE TABLE menu (
  item_id INTEGER PRIMARY KEY,
  type_id INTEGER,
  item_name TEXT,
  item_description TEXT,
  price INTEGER,
  FOREIGN KEY (type_id) REFERENCES types(type_id)
);
    """

    execute_query(connection, create_menu_table)

create_basket_table = """
    CREATE TABLE basket (
  basket_id INTEGER PRIMARY KEY,
  item_id INTEGER,
  user_id INTEGER,
  total INTEGER,
  FOREIGN KEY (item_id) REFERENCES menu(item_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);
    """

    execute_query(connection, create_basket_table)


create_users = """
    INSERT INTO
      users (user_name, user_surname, email, phone_number)
    VALUES
      ('James', 'Smith', '123@g', 123),
      ('Leila', 'Smith', '123@g', 123),
      ('Mike', 'Denmark', '123@g', 123);
    """

    execute_query(connection, create_users)

select_users = "SELECT * from users"

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
