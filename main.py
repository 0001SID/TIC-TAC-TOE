import os
from board import *
from check import *
from bot import *
import time
import sys
import random
print('\n\t\t\t\tTIC-TAC-TOE\n\n')
print("Choose Your game mode\n")
print("1.Multiplayer\n2.Single Player\n")
mode = input("Mode : ")
name = {}
if mode == '1':
    name['1'] = input("Enter the name of Player 1 : ").upper()
    name['2'] = input("Enter the name of Player 2 : ").upper()
else:
    name['1'] = input("Enter your name : ").upper()
    name['2'] = "Bot"
print('\n\t\t\t',name['1'],'is : O')
print('\t\t\t',name['2'],'is : X')
if mode == '2':
    while True:
        print('\n\nChoose level:')
        print('\n\t\t\t1.Easy\n\t\t\t2.Medium\n\t\t\t3.Hard')
        try:
            level = int(input('Level: '))
        except:
            print("\nPlease Enter a valid input (1/2/3)\n")
            continue
        if level not in range(1,4):
            print("\nPlease Enter a valid input (1/2/3)\n")
        else:
            break
    
    if level == 3:
        level = 6
    elif level == 2:
        level = 3
print_board(board)
loading(2,'Tossing')
toss = random.randint(1,2)
print('\t\t\t',name[str(toss)],'win the toss\n')
if toss == 1:
    player = '1'
    turn = 'O'
else:
    player = '2'
    turn = 'X'
for j in range(9):
    global position
    while True:
        print('\t\t\t',name[player]+'\'s turn \n')
        if mode == '1':
            position = input('Choose your position: ')
            if out_range(position) == True:
                print("Out of range")
                continue
            elif position_overload(board,position) == True:
                print("\t\t\tPosition is already accupied\n")
            else:
                break
        else:
            if player == '1':
                position = input('Choose your position: ')
                if out_range(position) == True:
                    print("\nOut of range\n")
                    continue
                if position_overload(board,position) == True:
                    print("\t\t\tPosition is already accupied\n")
                else:
                    break
            else:
                loading(2,'Thinking')
                position = bot_move(board,level)
                print('BOT choose:',position)
                break
    board[position] = turn
    print_board(board)
    if check_win(board) == True:
        print('\t\t\t',name[player],'Win\n\t\t\t Game Over')
        os._exit(0)
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
