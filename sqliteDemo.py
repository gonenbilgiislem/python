import sqlite3
import os
#%%
def SelectOperasuonlari():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("select * from customers where City ='Prague'")
    for row in cursor:
        print("First Name: ", row[1])
    connection.close()

SelectOperasuonlari()
#%%
def InsertCustomers():
    connection = sqlite3.connect('chinook.db')
    connection.execute("insert into customers (FirstName,LastName,City,Country,email) values ('Mehmet','Kaya','Istanbul','Turkey','ozensoft@gmail.com')")
    connection.commit()
    connection.close()

InsertCustomers()
#%%
def UpdateCustomers():
    connection = sqlite3.connect('chinook.db')
    connection.execute("update customers set City='Gönen' where CustomerId='62'")
    connection.commit()
    connection.close()

UpdateCustomers()
#%%
def DeleteCustomers():
    connection = sqlite3.connect('chinook.db')
    connection.execute("delete from customers where CustomerId='62'")
    connection.commit()
    connection.close()

DeleteCustomers()
#%%
def JoinOperasyonlari():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("select * from artists inner join albums a on artists.ArtistId = a.ArtistId")
    for row in cursor:
        print("Sanatçı : ",row[1], "Albüm Adı : ",row[3])
    connection.close()

JoinOperasyonlari()
