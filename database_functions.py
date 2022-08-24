import sqlite3 as sl
import os

def database_conection_func():

    if os.path.exists('boards.db') == 0:
        
        con = sl.connect('boards.db') # This line creates the actual database

        with con:
        #This section of code creates tables in the database
            con.execute("""
                    CREATE TABLE BOARDS(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Uniqid TEXT NOT NULL,
                        searialnumber TEXT NOT NULL,
                        hardwareid TEXT NOT NULL
                        );
                    """)
        #Once the database and tables have been made, the database creates a admin level account for the user
        con.commit()
        return con
    else:
        con = sl.connect('boards.db') # This line creates the actual database
        return con
