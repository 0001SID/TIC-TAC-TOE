from check import *
import sys
import time
blank_board = {'1':'1','2':'2','3':'3',
               '4':'4','5':'5','6':'6',
               '7':'7','8':'8','9':'9'}

def print_board(board):
    print(' ',board['1'],' | ',board['2'],' | ',board['3'],' ')
    print('-----+-----+-----')
    print(' ',board['4'],' | ',board['5'],' | ',board['6'],' ')
    print('-----+-----+-----')
    print(' ',board['7'],' | ',board['8'],' | ',board['9'],' ')
    print('-----+-----+-----')
def loading(length,name):
    for l in range(length):
        chars = '/-\|'
        for k in chars:
            sys.stdout.write("\r\t\t\t  "+name+" "+k)
            time.sleep(0.1)
    print("\n")