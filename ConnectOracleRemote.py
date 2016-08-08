import cx_Oracle
# con = cx_Oracle.connect('test/test@127.0.0.1/orcl')
dsnStr = cx_Oracle.makedsn("sgsnd-vdb08.asd.onstarlab.com", "1521", "SMRTGRDD")
con = cx_Oracle.connect(user="RIDESHARE", password="RIDESHARE", dsn=dsnStr)
print con.version
cur = con.cursor()
cur.execute('select * from RIDE_PREF where rownum <10')
for result in cur:
    print result
cur.close()
con.close()