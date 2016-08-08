import cx_Oracle
con = cx_Oracle.connect('test/test@127.0.0.1/orcl')
print con.version
cur = con.cursor()
cur.execute('select * from ALL_CONSTRAINTS where rownum <10')
for result in cur:
    print result
cur.close()
con.close()