from Player import gameplay
#Intialize the data
ply = gameplay()
draw = 0
game_count = 0
print("********THIS IS A BLACK JACK GAME************")


#Game started
while True:
    if game_count is 0:
        game_start = input("Entry 'y' for start 'n' for exit: ")

    if ply.money <= 0:
        print("game over")
        break

    if game_start is 'n' or draw is "b":
        break
    
    elif game_start is "y":
        ply.game_start(game_start)
        while True:
            #Drawing card or not
            draw = input("Hit for 'h' & Stand for 's' & break for 'b': ")        
            
            #Player hit so keep drawing card 
            if draw is 'h': 
                #drwa_card == 1 is player drawing crad
                ply.draw_card(1)
                print("Your number now is: {}".format(ply.player_num))
                if ply.player_num > 21:
                    ply.reset_game()
                    print("You bucks")
                    break
                    
            #Player stand so keep
            elif draw is 's':
                #Verify wins, losses or bucts
                ply.verify()
                break
            
            #End game
            elif draw is "b":
                break
            
            #Entry wrong number
            else:
                print("Please entry again")
    else:
        print("Please entry again")
    
    game_count += 1
