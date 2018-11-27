import os
from board import *
from check import *
from bot import *
import time
import sys
import random
import copy
while True:
    board = copy.copy(blank_board)
    print('\n\t\t\t\tTIC-TAC-TOE\n\n')
    while True:
        print("Choose Your game mode\n")
        print("1.Multiplayer\n2.Single Player\n")
        mode = input("Mode : ")
        if mode not in ['1', '2']:
            print("please choose a valid input (1/2)\n")
        else:
            break
    name = {}
    if mode == '1':
        name['1'] = input("Enter the name of Player 1 : ").upper()
        name['2'] = input("Enter the name of Player 2 : ").upper()
    else:
        name['1'] = input("Enter your name : ").upper()
        name['2'] = "BOT"
    print('\n\t\t\t', name['1'], 'is : O')
    print('\t\t\t', name['2'], 'is : X')
    if mode == '2':
        while True:
            print('\n\nChoose level:')
            print('\n\t\t\t1.Easy\n\t\t\t2.Medium\n\t\t\t3.Hard')
            try:
                level = int(input('Level: '))
            except:
                print("\nPlease Enter a valid input (1/2/3)\n")
                continue
            if level not in range(1, 4):
                print("\nPlease Enter a valid input (1/2/3)\n")
            else:
                break

        if level == 3:
            level = 6
        elif level == 2:
            level = 3
    print_board(board)
    loading(2, 'Tossing')
    toss = random.randint(1, 2)
    print('\t\t\t', name[str(toss)], 'win the toss\n')
    if toss == 1:
        player = '1'
        turn = 'O'
    else:
        player = '2'
        turn = 'X'

    for j in range(9):
        global position
        while True:
            print('\t\t\t', name[player]+'\'s turn \n')
            if mode == '1':
                position = input('Choose your position: ')
                print('\n')
                if out_range(position) == True:
                    print("Out of range")
                    continue
                elif position_overload(board, position) == True:
                    print("\t\t\tPosition is already accupied\n")
                else:
                    break
            else:
                if player == '1':
                    position = input('Choose your position: ')
                    print('\n')
                    if out_range(position) == True:
                        print("\nOut of range\n")
                        continue
                    if position_overload(board, position) == True:
                        print("\t\t\tPosition is already accupied\n")
                    else:
                        break
                else:
                    if j == 1 and (position in ['1', '3', '7', '9']) and level == 6:
                        position = '5'
                    else:
                        position = bot_move(board, level)
                    print('\nBOT choose:', position, '\n')
                    break
        board[position] = turn
        print_board(board)
        if check_win(board) == True:
            print('\t\t\t', name[player], 'Win\n\t\t\t Game Over')
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if player == '1':
            player = '2'
        else:
            player = '1'
        if j == 8:
            print('\n\t\t\tMatch tie no one win')
    print("\nDo you want to play again? (Y/N)")
    res = input()
    if res == 'y':
        continue
    else:
        break
