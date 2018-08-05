import sqlite3
import sys

option = sys.argv[1]
userName = sys.argv[2]
password = sys.argv[3]

# Add account into database
def addAccount(userName, password):
    sql = sqlite3.connect("userInfo.db")

    c = sql.cursor()

    c.execute("""INSERT INTO USERINFO (userName,password,money) VALUES
                 ('{}','{}',{})""".format(userName,password,1000))

    sql.commit()
    sql.close()

    print("Create a new account sucessfully.")

def deleteAccount(userName, password):
    sql = sqlite3.connect("userInfo.db")

    c = sql.cursor()
    passwordInfo = c.execute(""" SELECT * From USERINFO""")

    for user in passwordInfo:
        print(user[0],user[1])
        if user[0] == userName and user[1]==password:
            c.execute("DELETE * FROM USERINFO WHERE userName='{}', password='{}'".format(userName,password))
            print("Sucessfully delete account")
            break

    else:
        print("The username or password doesn't exit")

    sql.commit()
    sql.close()

if option == "-n":
    if len(userName) >= 7 and len(password) >= 7:

        # for char in charUserName:

        if (userName+password).isalnum() is False:
            print("Your username and password only can have number and alphabet")

        else:
            verify = input("Please Entry you password again: ")

            if password != verify:
                print("The password you input doesn't match.")
            else:
                addAccount(userName, password)

    else:
        print("Length Error : The user name and Password Length have to be more the 7 and only content alphabet and numbers")

elif option == "-d":
    deleteAccount(userName, password)
