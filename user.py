import sqlite3


def GetUserInfo(userName, password):
    sql = sqlite3.connect("userInfo.db")
    c = sql.cursor()
    c.execute("""SELECT *  FROM USERINFO WHERE userName='{}' AND password='{}'""".format(userName, password))
    userInfo = c.fetchall()

    if userInfo:
        return True
    else:
        return False

def Login():
    # Login with account
    # User have three time chance try their user name and password
    for i in range(3):
        print("Input exit end this game")
        userName = input("Your User Name : ")

        if userName == "exit":
            break

        password = input("Your password : ")
        print("\n")

        verify = GetUserInfo(userName, password)

        if verify:
            return True

        print("Please entry again")

    else:
        print("Too many try error")
