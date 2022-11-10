import sqlite3
import os

nw_db = sqlite3.connect("new_db.db")
db_cur = nw_db.cursor()
db_cur.execute("SELECT * FROM users")
nw = db_cur.fetchall()

for n in nw:
    print('\n:     ', n)

nw_db.commit()
nw_db.close()