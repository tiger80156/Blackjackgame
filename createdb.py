import sqlite3

conn = sqlite3.connect('userInfo.db')

c = conn.cursor()

c.execute('''CREATE TABLE   USERINFO
       (userName     CHAR(30)    NOT NULL,
       password     CHAR(30)   NOT NULL,
       money    INT NOT NULL);''')


conn.commit()
conn.close()