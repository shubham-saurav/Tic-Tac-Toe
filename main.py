import os
import time
import random


board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_header():
    print(
    """
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\

 

""")

def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("   |   |   ")


def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False


def is_board_full(board):
    if " " in board:
        return False
    else:
        return True


def get_computer_move(board, player):
    if board[5] == " ":
        return 5

    while True:
        move = random.randint(1, 9)
        if board[move] == " ":
            return move
            break

    return 5


while True:
    os.system("cls")
    print_header()
    print_board()

    choice = input("Please choose an empty space for X. ")
    choice = int(choice)

    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)

    if is_winner(board, "X"):
        os.system("cls")
        print_header()
        print_board()
        print("X wins! Congratulations")
        break

    os.system("cls")
    print_board()

    if is_board_full(board):
        print("Tie!")
        break

    choice = get_computer_move(board, "O")

    if board[choice] == " ":
        board[choice] = "O"
    else:
        print
        "Sorry, that space is not empty!"
        time.sleep(1)

    if is_winner(board, "O"):
        os.system("cls")
        print_header()
        print_board()
        print("O wins! Congratulations")
        break

    if is_board_full(board):
        print("Tie!")
        break
