import small_database.database_functions as df

con = df.database_conection_func()

id_num = input('ID: ')
serial_number = input('Serial: ')
hardware_id = input('hardware id: ')

con.execute(f'INSERT INTO BOARDS VALUES ( NULL, "{id_num}","{serial_number}","{hardware_id}")')
con.commit()

for row in con.execute('SELECT * FROM BOARDS'):
    print(f'Database ID: {row[0]}')
    print(f'Real ID: {row[1]}')
    print(f'Serial Number: {row[2]}')
    print(f'Hardware ID: {row[3]}')