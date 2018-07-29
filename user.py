import sqlite3


# class User():
#     def __init__(self,userName,password):
#         self.userName = userName
#         self.password = password

def GetUserInfo(userName, password):
    sql = sqlite3.connect("userInfo.db")
    c = sql.cursor()
    data = c.execute("""SELECT *  FROM USERINFO""")
    for user in data:
        if user[0] == userName and user[1] == password:
            return True
    else:
        return False

def Login():
    # Login with account
    # User have three time chance try their user name and password
    i = 0
    while i<3:
        print("Input exit end this game")
        userName = input("Your User Name : ")

        if userName == "exit":
            break

        password = input("Your password : ")
        print("\n")


        verify = GetUserInfo(userName, password)
        i+=1

        if verify:
            return True

        print("Please entry again")

    else:
        print("Too many try error")


def Signup(userName, password):

