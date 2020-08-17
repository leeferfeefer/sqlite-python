import sqlite3
from sqlite3 import Error


def main():
    # r in string means "raw string"
    connection = create_connection(r"pythonsqlite.db")

    # create tables
    if connection is not None:

        table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

        create_table(connection, table)
    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn
    # finally:
    #     if conn:
    #         conn.close()


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
