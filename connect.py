import pyodbc
import time
import datetime

#tcp:
server = 'server'
database = 'dbname'
username = 'username'
password = 'password'
table_name = 'tablename'


cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

query = f'exec sp_columns [{table_name}]'
cursor.execute(query)
row = cursor.fetchall()

table_names = [i[3] for i in row]
FORMAT = '{:10} {:^25} {:^25} {:^25} {:3}|{:3}|{:3}|{:3}|{:3}|{:3} : {:12},{:12},{:12} [{}]'

header = FORMAT.format(*table_names)
print(header)
print('_'*len(header))
time.sleep(5)

now = datetime.datetime.now()
cursor.execute("SELECT * FROM CADU")
row = cursor.fetchone()
bg = ('\033[01;47m',' ','\033[00m')
while row:
    row = tuple(map(str, row))
    row = tuple(map(str.strip, row))
    text = FORMAT.format(*row) 
    print(*bg, text,*bg)
    print('\033[01;42m',' '*(len(text)+6),'\033[00m')
    row = cursor.fetchone()
print('Term Time:', str(datetime.datetime.now() - now))
