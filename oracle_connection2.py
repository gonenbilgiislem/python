import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="GONSON", password="GONEN",
                               dsn="192.168.0.43/YERELDEV")

# Obtain a cursor
cursor = connection.cursor()

# Data for binding
ADA = input(str("ADA Giriniz: "))
PARSEL = input(str("PARSEL Giriniz: "))

# Execute the query
sql = """SELECT *
         FROM GYS_BEYAN
         WHERE ADA = :A_ADA AND PARSEL = :X_PARSEL"""
cursor.execute(sql, A_ADA=ADA, X_PARSEL=PARSEL)

# Loop over the result set
for row in cursor:
    print(row)