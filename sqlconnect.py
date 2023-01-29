import pyodbc

server = '212.156.58.246'
database = 'Data1'
username = 'chatgpt'
password = 'Cg.123456'
port = 1433

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';port='+str(port))
cursor = conn.cursor()

cursor.execute("SELECT * FROM gruplar")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

conn.close()
