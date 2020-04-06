#Making a game of Tic Tac Toe
#Take one Board as below
board2 = ['.','.','.',
         '.','.','.',
         '.','.','.']
def display_board2():
    print("    Actual Game          Reference Position")
    print("  _____________          _____________")
    print("  | {} | {} | {} |          | 1 | 2 | 3 |".format(board2[0],board2[1],board2[2]))
    print("  |___|___|___|          |___|___|___|")
    print("  | {} | {} | {} |          | 4 | 5 | 6 |".format(board2[3],board2[4],board2[5]))
    print("  |___|___|___|          |___|___|___|")
    print("  | {} | {} | {} |          | 7 | 8 | 9 |".format(board2[6],board2[6],board2[8]))
    print("  |___|___|___|          |___|___|___|")

display_board2()
