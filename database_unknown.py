import sqlite3 as sl
import os

con = sl.connect('boards')

for row in con.execute('SELECT * FROM BOARDS'):
    print(f'Unique ID: {row[0]}')
    print(f'Serial Number: {row[1]}')
    print(f'Hardware ID: {row[2]}')