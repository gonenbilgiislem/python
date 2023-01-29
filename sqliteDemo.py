import sqlite3
import os
def SelectOperasuonlari():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("select * from customers where City ='Prague'")
    for row in cursor:
        print("First Name: ", row[1])
    connection.close()

SelectOperasuonlari()
