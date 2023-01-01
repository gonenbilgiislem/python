#sql server bağlantısı

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=SQLSERVER;'
                        'Database=Test;'
                        'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT * FROM Test.sunnet_listesi.personel')

for row in cursor:
# write the output to a file export.csv
    with open('export.csv', 'a') as f:
        f.write(str(row))
        f.write('')
        f.close()
