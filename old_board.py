#Making a game of Tic Tac Toe
#Take one Board as below
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

#           ************   Displaying Board    ******************
def display_board():
    print("    Actual Game       Reference Position")
    print("  ---------------     ------------------\n",end="")
    print("  ",board[0]," | ",board[1]," | ",board[2],"       1 | 2 | 3")
    print("  ---------------      -----------")
    print("  ",board[3]," | ",board[4]," | ",board[5],"       4 | 5 | 6")
    print("  ---------------      -----------")
    print("  ",board[6]," | ",board[7]," | ",board[8],"       7 | 8 | 9")
    #print(""--------------------      -------------")
    print('\n\n')
display_board()
