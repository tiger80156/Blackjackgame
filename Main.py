from cardDrawer import CardBox,Card
from player import PlayerInfo
from Login import login, signup
import os


log = input("\"s\" for sign up\n Any key login")

#Sign up
if log == "s":
    userName = input("Your User Name : ")
    password = input("Your password : ") 
    signup(userName,password)
    gameStart = True

# Login with account
# Input More than three 
i = 0
while i<3:
    print("Input exit end this game")
    userName = input("Your User Name : ")

    if userName == "exit":
        break 

    password = input("Your password : ")
    print("\n")

    User = login(userName,password)
    verify = User.getUserInfo()
    i+=1

    if verify:
        break
    print("Please entry again")

else:
    print("Too many try error")
    os.system("Pause")



if verify:
    # Start Input  
    print("""********THIS IS A BLACK JACK GAME************
    The Game Rule:                      """)

    gameStart = input("Entry \"y\" for game Start \"n\" for game end: ").strip()

    if gameStart is "y":

        while True:
            try:
                playerNum = eval(input("Please input the player number : "))
                break
            except:
                print("Player Number have to be a number")
        # Initialize the Card Box and Player Info
        card = CardBox(playerNum)

        
        while True:
        # Draw Card 
        # H for hint S for stand
            for i in range(playerNum):
                print("***It time for player{}***".format(i+1))
                print("Your chips Number Now : ",card.money[i])
                card.setPlayerNum(i)

                while True:
                    try:
                        yourDealer = eval(input("How many deal you want to use this time : "))
                        print(end='\n')
                        break

                    except:
                        print("It must be a number")
                    
                # Game Started
                b = card.choiceCard(yourDealer)    

                if b == "b":
                    break
                
            # Check winner
            card.checkWinner()








