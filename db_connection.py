import sqlite3
from sqlite3 import Error


def main():
    # r in string means "raw string"
    connection = create_connection(r"pythonsqlite.db")

    # create table
    if connection is not None:

        projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

        create_table(connection, projects_table)

        tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                          id integer PRIMARY KEY,
                                          name text NOT NULL,
                                          priority integer,
                                          status_id integer NOT NULL,
                                          project_id integer NOT NULL,
                                          begin_date text NOT NULL,
                                          end_date text NOT NULL,
                                          FOREIGN KEY (project_id) REFERENCES projects (id)
                                      );"""

        create_table(connection, tasks_table)
    else:
        print("Error! cannot create the database connection.")

    with connection:
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(connection, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(connection, task_1)
        create_task(connection, task_2)


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


def create_project(connection, project):
    """
    Create a new project into the projects table
    :param connection:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = connection.cursor()
    cur.execute(sql, project)
    connection.commit()
    return cur.lastrowid


def create_task(connection, task):
    """
    Create a new task
    :param connection:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = connection.cursor()
    cur.execute(sql, task)
    connection.commit()
    return cur.lastrowid

if __name__ == '__main__':
    main()
