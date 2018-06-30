import sqlite3
from cardDrawer import CardBox

class login():
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password

    def getUserInfo(self):
        sql = sqlite3.connect("userInfo.db")
        c = sql.cursor()
        data = c.execute("""SELECT *  FROM USERINFO""")
        for user in data:
            if user[0] == self.userName and user[1] == self.password: 
                return True

class signup():
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

        sql = sqlite3.connect("userInfo.db")

        c = sql.cursor()

        c.execute("""INSERT INTO USERINFO (userName,password,money) VALUES 
                     ('{}','{}',{})""".format(userName,password,1000))

        sql.commit()
        sql.close()