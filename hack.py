import sqlite3

conn = sqlite3.connect("user.db")
c = conn.cursor()

c.execute("SELECT * FROM account")
lst = c.fetchall()
conn.commit()


print(lst)

conn.close()