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

        # update task
        # update_task(connection, (2, '2015-01-04', '2015-01-06', 2))

        # delete task
        # delete_task(connection, 2)
        # delete_all_tasks(connection)

        print("1. Query task by priority:")
        select_task_by_priority(connection, 1)

        print("2. Query all tasks")
        select_all_tasks(connection)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param connection: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = connection.cursor()
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


def update_task(connection, task):
    """
    update priority, begin_date, and end date of a task
    :param connection:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = connection.cursor()
    cur.execute(sql, task)
    connection.commit()


def delete_task(connection, id):
    """
    Delete a task by task id
    :param connection:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = connection.cursor()
    cur.execute(sql, (id,))
    connection.commit()


def delete_all_tasks(connection):
    """
    Delete all rows in the tasks table
    :param connection: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = connection.cursor()
    cur.execute(sql)
    connection.commit()


def select_all_tasks(connection):
    """
    Query all rows in the tasks table
    :param connection: the Connection object
    :return:
    """
    cur = connection.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
