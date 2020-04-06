
#   ***********  Let's play a tic-tac-toe game  *******************

#    Auther:    Milan Garain

#Making a game of Tic Tac Toe
#Take one Board as below
board = ['.','.','.',
         '.','.','.',
         '.','.','.']

#  Player 1 is 'X'  and Player 2 is 'O'
players = ['X','O']

#Player who is going to make move
# '0' refers to Player 1 ('X') and '1' refers to Player 2 ('O')
current_player = 0

#displaying Winner or game is tie
winner = None


#           ************   Displaying Board    ******************
def display_board():
    print()
    print("    Actual Game          Reference Position")
    print("  _____________          _____________")
    print("  | {} | {} | {} |          | 1 | 2 | 3 |".format(board[0],board[1],board[2]))
    print("  |___|___|___|          |___|___|___|")
    print("  | {} | {} | {} |          | 4 | 5 | 6 |".format(board[3],board[4],board[5]))
    print("  |___|___|___|          |___|___|___|")
    print("  | {} | {} | {} |          | 7 | 8 | 9 |".format(board[6],board[7],board[8]))
    print("  |___|___|___|          |___|___|___|")
    print("\n")

#        **************   Taking position and validating   *********
#function to take a valid position
#incase invalid position take again until a valid position taken
def take_position():
    valid_pos = False
    while(True):
        position = input()
        # Validating input is Number or not
        #if its not a number it will through a Error(ValueError)
        #again validate if entered number is valid and empty positioned
        try:
            pos = int(position)-1           #Making absolute position(0 index)
            if(pos<0 or pos>8):
                print("Player",current_player+1,"Please enter a valid position (in range[1-9])",end="  ")
            elif(board[pos]!='.'):
                print("Player",current_player+1,"Please enter an empty position",end="  ")
            else:
                return pos
        except ValueError:
            print("Player",current_player+1,"Please enter a Number(in range[1-9])",end="  ")


#      ************    Condition for Tied Game      *****************
#checking if game has tied
#if any position is empty then it's not tied
def is_game_tied():
    for i in range(9):
        if(board[i] == '.'):
            return False
    return True

#Checking row for winner
def check_row():
    #row1 = board[0]==board[1]==board[2] != '-' ...
    if((board[0]==board[1]==board[2] != '.')
    or (board[3]==board[4]==board[5] != '.')
    or (board[6]==board[7]==board[8] != '.')):
        return True
    return False

#Checking column for winner
def check_column():
    #we can break like
    #col1 = board[0]==board[3]==board[6] != '-' and so on
    if((board[0]==board[3]==board[6] != '.')
    or (board[1]==board[4]==board[7] != '.')
    or (board[2]==board[5]==board[8] != '.')):
        return True
    return False

#Checking diaginal for winner
def check_diagonal():
    #we can break like
    #diag1 = board[0]==board[4]==board[8] != '-' and so on
    if((board[0]==board[4]==board[8] != '.')
    or (board[2]==board[4]==board[6] != '.')):
        return True
    return False

# **************  Checking if someone has won the game   *****************
#if any row or column or diagonal is taken by one player then he is winner
#we need not store winner because current player will be winner incase someone won
def is_someone_won():
    if(check_row() or check_column() or check_diagonal()):
        return True
    return False


#**************      Checking if Game Ended     ****************
#checking someone won the game or it's tied
def game_over():
    global winner
    if(is_someone_won()):
        winner = True
        return True
    if(is_game_tied()):
        return True
    return False


#    *************   Change Current Player     *************
#Changing player who will move next one
def flip_player():
    global current_player
    current_player = 1 - current_player


#    ************      Updating Board        ******************
#updating board when a player mon=ved a position
def update_board(position):
    global current_player
    board[position] = players[current_player]


#     ******************   Game Started     ***************
#orginal game
def play_game():
    display_board()
    #Game will on until someone win or tied
    while(True):
        #Taking positon of current player
        print("Player",current_player+1,"please select your position [1-9]",end="  ")
        position = take_position()
        #update board and show it
        update_board(position)
        display_board()
        # Game Ending condition
        if(game_over()):
            break
        # Changing player
        flip_player()

    #Displaying Result
    if(winner):
        print("Player {0}({1}) is winner".format(current_player+1,players[current_player]))
    else:
        print("Nice played but game is tied")
    print("Play Again\n")


#       ************   Calling Game       ********************
play_game()
