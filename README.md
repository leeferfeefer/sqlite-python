# SQLite DB for Python


https://www.sqlitetutorial.net/sqlite-python/creating-database/



## Virtual Environment:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Create: `python3 -m venv env`   
Run: `source env/bin/activate`

## Commands:
First run:    
`sqlite3 ./pythonsqlite.db`   
`.header on`   
`.mode column`
   
To view tables: `.tables`

To view records:   
`SELECT * FROM projects;`   
`SELECT * FROM tasks;`