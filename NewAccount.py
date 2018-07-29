import sqlite3
import sys


userName = sys.argv[1]
password = sys.argv[2]




def addaccount(userName, password):
    sql = sqlite3.connect("userInfo.db")

    c = sql.cursor()

    c.execute("""INSERT INTO USERINFO (userName,password,money) VALUES
                 ('{}','{}',{})""".format(userName,password,1000))

    sql.commit()
    sql.close()

    print("Create a new account sucessfully.")

if len(userName) >= 7 and len(password) >= 7:

    # for char in charUserName:

    if (userName+password).isalnum() is False:
        print("Your username and password only can have number and alphabet")

    else:
        verify = input("Please Entry you password again: ")

        if password != verify:
            print("The password you input doesn't match.")
        else:
            addaccount(userName, password)

else:
    print("Length Error : The user name and Password Length have to be more the 7 and only content alphabet and numbers")
