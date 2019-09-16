# Lekezelni a user hibait

# Mukodjon

# Egyszeru

# alap jatek szabaly

# .txt file ---> update on every turn 
game = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]






def display_game_board():
        print(game[0] + " | " + game[1] + " | " + game[2])    
        print(game[3] + " | " + game[4] + " | " + game[5])    
        print(game[6] + " | " + game[7] + " | " + game[8])           
display_game_board()   


def check_if_game_over():
        return False
        

# Kezd egy uj jatekot

def play_game():
        display_game_board()









# X_Player = player who chooses "X"
# WINNING script
def X_Winner():
        if  game[0] == "X" and game[1] == "X" and game[2] == "X":
        # Player1 = X_Player ,  hogyha player1 "X"-el kezd.
                check_if_game_over == True

        elif  game[3] == "X" and game[4] == "X" and game[5] == "X":
                check_if_game_over == True

        elif  game[6] == "X" and game[7] == "X" and game[8] == "X":
                check_if_game_over == True

        elif  game[0] == "X" and game[4] == "X" and game[8] == "X":
                check_if_game_over == True

        elif  game[6] == "X" and game[4] == "X" and game[2] == "X":
                check_if_game_over == True

# global variable == Winner


def O_Winner():
        if  game[0] == "O" and game[1] == "O" and game[2] == "O":
                check_if_game_over == True
                is_O_the_winner == True
        elif  game[3] == "O" and game[4] == "O" and game[5] == "O":
                check_if_game_over == True
                is_O_the_winner == True

        elif  game[6] == "O" and game[7] == "O" and game[8] == "O":
                check_if_game_over == True
                is_O_the_winner == True

        elif  game[0] == "O" and game[4] == "O" and game[8] == "O":
                check_if_game_over == True
                is_O_the_winner == True

        elif  game[6] == "O" and game[4] == "O" and game[2] == "O":
                is_O_the_winner == True
                
                check_if_game_over == True
        

# game_still_going MEGNEZNI megy-e meg a jatek
        game_still_going = False

def is_O_the_winner():
        if True:
                print("The winner is {}".format(O_Player))

def is_X_the_winner():
        if True:
                print("The winner is {}".format(X_Player))












