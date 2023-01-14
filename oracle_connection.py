import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
con = cx_Oracle.connect(user="GONSON", password="GONEN",
                               dsn="192.168.0.43/YERELDEV")

cur = con.cursor()
cur.execute("select * from gen_kisi order by kod")
res = cur.fetchall()
for row in res:
    print(row)

cur.close()
con.close()
