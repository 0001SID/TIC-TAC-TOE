from check import *
from board import *
import copy
import random
blank_positions = []


def revolutin(board):
    for i in range(1, 10, 3):
        score = 0
        if board[str(i)] == board[str(i+1)] == board[str(i+2)]:
            if board[str(i)] == 'X':
                score = 1
                break
            else:
                score = -1
                break
    for i in range(1, 4):
        if board[str(i)] == board[str(i+3)] == board[str(i+6)]:
            if(board[str(i)] == 'X'):
                score = 1
                break
            else:
                score = -1
                break
    if board[str(1)] == board[str(5)] == board[str(9)]:
        if(board[str(1)] == 'X'):
            score = 1
        else:
            score = -1
    if board[str(3)] == board[str(5)] == board[str(7)]:
        if(board[str(3)] == 'X'):
            score = 1
        else:
            score = -1
    return score


def bot_move(board, level):
    position = myturn_probability(board, 0, 'bot', level)
    # print('position',position)
    return position


def myturn_probability(board, depth, who, level):
    blank_positions = check_blank_position(board)
    hit = 0
    position = 0
    check = []
    probability = 0
    if who == 'bot':
        loading(0, 'Thinking')
    for i in blank_positions:  # Loop to check if there is any position to win for X
        board_copy = copy.copy(board)
        board_copy[str(i)] = 'X'
        if revolutin(board_copy) == 1:
            probability = 100
            position = i
            hit = 1
            break
    if hit == 0:  # If there is no any winning position then check one more level
        for i in blank_positions:
            if(who == 'bot'):
                loading(0, 'Thinking')
            board_copy = copy.copy(board)
            board_copy[str(i)] = 'X'
            if depth == level:  # if The depth of finding probability and no any winning position there then return Zero probability.The greater the level the deeper the program will calculate
                probability = 0
            else:  # If there is no any position for X to win 100% then check in which position there is the best probability of winning
                # This is the probabilities to win for that X move
                probability = opponent_turn_probability(
                    board_copy, level, depth)
                if who == 'bot':
                    check.append(probability)
    if who == 'bot':
        if hit == 1:
            return position  # If there is a position where the probability of winning is 100 then return that position
        else:  # If there is no any position for X to win 100% then check in which position there is the best probability of winning
            max_value = check[0]
            # print('check',check)
            position = blank_positions[0]
            j = 0
            for i in blank_positions:  # Check in which position we are getting the best probability to win
                if check[j] > max_value:
                    max_value = check[j]
                    position = i  # Return the best probability position
                j += 1
            return position

    return probability


def opponent_turn_probability(board, level, depth):
    # Check all the blank position in the board that we have now
    blank_positions = check_blank_position(board)
    temp = 0
    length = 0
    hit = 0
    for i in blank_positions:
        board_copy = copy.copy(board)
        board_copy[str(i)] = 'O'
        # If we find anny position of winnig for the opponent then there the probability of winning is negetive,and here -100
        if revolutin(board_copy) == -1:
            probability = -100
            hit = 1
            break
    if hit == 0:
        for i in blank_positions:
            board_copy = copy.copy(board)
            board_copy[str(i)] = 'O'
            # Check the next level for X if there is a situation for X to win if yes probability is 100 other wise calculate
            temp += myturn_probability(board_copy, depth+1, 'opponent', level)
            length += 1
        if temp == 0:
            probability = 0
        else:
            # This is the probability of winning for a X move with all the possible value of O
            probability = (temp/(length*100))*100
    return probability
