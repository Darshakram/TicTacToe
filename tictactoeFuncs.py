# Project 3 - Tic-Tac-Toe Simulator
# Name: Darcy Eliasi
# Instructor: S. Einakian 
# Section: 11
# Functions definitions comes here

from random import randint


# Welcome function for the project
# none -> int
def welcome():
    print("Welcome to this Tic-Tac-Toe Simulator.")
    print("Your goal is to line up 3 of your tics in either a line or a diagonal.")
    print("You will pick either X or O. X will go first.")
    versus = input("Do you wish to play against a (1)computer, or with (2)Players?")
    while versus != "1" and versus != "2":
        print("Answer not valid, please try again.")
        versus = input("Do you wish to play against a (1)computer, or with (2)Players?")
    return versus


# Makes the board that shows the positions of each spot
# none -> list
def create_board():
    testboard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for x in testboard[0:2]:
        print(x, "|", end=" ")
    print(testboard[2])
    print("---------")
    for y in testboard[3:5]:
        print(y, "|", end=" ")
    print(testboard[5])
    print("---------")
    for z in testboard[6:8]:
        print(z, "|", end=" ")
    print(testboard[8])
    return testboard


# Prints the blank board
# none -> list
def print_board(board):
    for x in board[0:2]:
        print(x, "|", end=" ")
    print(board[2])
    print("---------")
    for y in board[3:5]:
        print(y, "|", end=" ")
    print(board[5])
    print("---------")
    for z in board[6:8]:
        print(z, "|", end=" ")
    print(board[8])

    return board


# Player picks the letter
# none -> str
def pick_letter():
    letter = input("Choose X or O:")
    while (letter != "X") and (letter != "O") and (letter != "x") and (letter != "o"):
        letter = input("Can you please try again?")
    if letter == "x":
        letter = "X"
    elif letter == "o":
        letter = "O"
    return letter


# Takes the move and checks to see if it a valid move
# int -> list
def get_input(board, letter):
    move = int(input("Where would you like to place your letter (pick in range of 1-9): "))
    while move not in range(1, 10) or board[move - 1] != " ":
        print("Please choose another location.")
        move = int(input("Can you please try again?"))
    board[move - 1] = letter
    return board


# chooses a random location for when you play with the computer
# strlist -> list
def comp_mode(board, letter2):
    while True:
        move = randint(0, 8)
        if board[move] == " ":
            board[move] = letter2
            break
    return board


# Checks to see if X or O is the winner using the rows
# listlistlist -> str
def check_rows(board):
    if board[0] == board[1] == board[2] and board[0] != " ":
        return True
    if board[3] == board[4] == board[5] and board[3] != " ":
        return True
    if board[6] == board[7] == board[8] and board[6] != " ":
        return True
    return False


# Checks to see if X or O is the winner using the columns
# listlistlist -> str
def check_cols(board):
    if board[0] == board[3] == board[6] and board[0] != " ":
        return True
    if board[1] == board[4] == board[7] and board[1] != " ":
        return True
    if board[2] == board[5] == board[8] and board[2] != " ":
        return True
    return False


# Checks to see if X or O is the winner using diagonals
# listlistlist -> str
def check_diags(board):
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        return True
    return False


# Checks to see if there is a winner and then displays the winner's name
# liststr -> str
def check_win(board):
    if check_rows(board):
        return True
    elif check_cols(board):
        return True
    elif check_diags(board):
        return True
    return False


# Checks to see if the board is full
# list -> bool
def board_full(board):
    for x in board:
        if x == " ":
            return False
    return True
