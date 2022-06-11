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
board=["1","2","3",
        "4","5","6",
        "7","8","9"] 
        
        #if game still going
game_still_going = True
    #who won or tie the game 
winner = None
#next player
current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print('-+-+-')
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print('-+-+-')
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

def play_game():

    #display initial board
    display_board()
    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()
    #game over
if winner == "X" or winner =="O":
    print(winner)+ "You "
elif winner == None:
    print('Tie')

    
        


    #handle_turn(player)
    #get position from the player as str 
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position)-1

    #get x from the user to fill the board
    board[position] = "X"
    display_board()
    



def check_if_game_over():
    check_if_win()
    check_if_tie()

#return X or O
def check_if_win():
    #check rows
    rows_winner = check_rows()
    #check columns
    columns_winner = check_column()
    #check diagonal
    diagonal_win = check_diagonals()
    return

def check_rows():
    return

def check_column():
    return
def check_diagonals():
    return

def check_if_tie():
    return

    #flip player fro x to o
def flip_player():
    return




play_game()

