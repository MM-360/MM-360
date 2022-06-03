# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:08:45 2022

@author: Mitesh Mistry

project: Noughts & Crosses - 2022-06-03
"""
import random

def grid(n):
    
    board = []
    
    for i in range(n):
        board.append("-")
    return board


board1 = grid(9)

# def display_grid(board):
    
#test =  ["+----","+----","+----"]
# print("+----")
# print("  X  ", "  O  ")
#print(*test, sep = '\n')


# val = input("Enter your value: ")
# print(val)
    



print(board1)

#board1 = ['X', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'X']

p1 = input("Enter your value X or O: ")

if p1 =='X':
    p2 = 'O'
else:
    p2 = 'X'






def check_column(board, p, pos):
    if board[pos + 3*0] == p:
        if board[pos+3*1] == p:        
            if board[pos+3*2] == p:        
                return True
            
def check_row(board, p, pos):
    if board[pos + 0] == p:
        if board[pos + 1] == p:        
            if board[pos + 2] == p:        
                return True

def check_dig1(board, p, pos):
    if board[pos + 0] == p:
        if board[pos + 2] == p:        
            if board[pos + 4] == p:        
                return True


def check_dig2(board, p, pos):
    if board[pos + 0] == p:
        if board[pos + 4] == p:        
            if board[pos + 8] == p:        
                return True

 
def check_win(board, player):
    
    length = len(board)
    #column check
    for i in range(3):
        if check_column(board, player,i):
            print('col')
            return True
        
    for i in range(0,7,3):
        if check_row(board, player,i):
            print('col')
            return True
        
    if check_dig1(board, player, 2):
        print('diag1')
        return True
    
    if check_dig2(board, player, 0):
        print('diag2')
        return True

    return False




while True:
    #val, pos = input("Enter two values: ").split(',')
    position = input("P1 enter your position: ")
    
    board1[int(position)-1] = p1
    
    print(board1)
    
    if check_win(board1,p1):
        print('P1 has won')
        print(board1)
        break
    
    
    if board1.count('X') + board1.count('O')  == 9:
        print("Tie!")
        break
    
    position = input("P2 enter your position: ")
    
    board1[int(position)-1] = p2
    
    print(board1)
    
    if check_win(board1,p2):
        print('P2 has won')
        print(board1)
        break

    if board1.count('X') + board1.count('O')  == 9:
        print("Tie!")
        break

# check_win(board1, 'O')
# print(board1)