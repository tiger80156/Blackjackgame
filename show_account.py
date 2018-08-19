import sqlite3

sql = sqlite3.connect("userInfo.db")
c = sql.cursor()
c.execute("""SELECT * FROM USERINFO""")
userInfo = c.fetchall()

for (userName,password,money) in userInfo:
    print(userName[0]+(len(userName)-2)*'*'+userName[-1], password[0]+(len(password)-2)*'*'+password[-1])
