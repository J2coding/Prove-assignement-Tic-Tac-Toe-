import random
"""
overview
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.


Requirements
Your program must also meet the following requirements.

The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main.



"""
#Required 
#board
#functions:-
    #display_board
    #play_game
    #check_win
    #check_rows
    #check_columns
    #check_diagonals
    #check_tie
    #flip player

    #Game board
board=["1","2","3","4",

        "5","6","7","8","9"] 
def main():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print('-+-+-')
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print('-+-+-')
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")
    

main()

