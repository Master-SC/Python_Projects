# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:53:01 2020

@author: TCS WFH
"""



def display_board(board):
    print('\n'*100)
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("- - -")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("- - -")
    print(board[1]+"|"+board[2]+"|"+board[3])

  
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position): 
    board[position]=marker
    

def win_check(board, mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
(board[4]==mark and board[5]==mark and board[6]==mark) or
(board[7]==mark and board[8]==mark and board[9]==mark) or
(board[1]==mark and board[4]==mark and board[7]==mark) or
(board[2]==mark and board[5]==mark and board[8]==mark) or
(board[3]==mark and board[6]==mark and board[9]==mark) or
(board[1]==mark and board[5]==mark and board[9]==mark) or
(board[3]==mark and board[5]==mark and board[7]==mark)) 

import random

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    if board[position]==' ':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def replay():
    choice="Wrong"
    while choice not in ['Y','N']:
        
        choice=input("Do you want to Replay..'Y' or 'N' : ")
        
        if choice in ['Y','N']:
            if choice=='Y':
                return True
            else:
                return False
        else:
            print("Please Choose between 'Y' or 'N' ")







print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    Gme_list = [' '] * 10
    Player1_Mrker, Player2_Mrker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game=input("You are Ready for the Game... Y or N ??")
    
    if play_game[0].lower()=='y':
        Game_on=True
    else:
        Game_on=False

   
    while Game_on:
        
        if turn=='Player 1':
            display_board(Gme_list)
            position=player_choice(Gme_list)
            place_marker(Gme_list, Player1_Mrker, position)
            
            if win_check(Gme_list, Player1_Mrker):
                display_board(Gme_list)
                print(" Congrts Player 1 won the Game .....")
                Game_on=False
                
            else:
                if full_board_check(Gme_list):
                    display_board(Gme_list)
                    print(" The Match is draw .....")
                    break
                else:
                    turn='Player 2'
                    
        else:
            display_board(Gme_list)
            position=player_choice(Gme_list)
            place_marker(Gme_list, Player2_Mrker, position)
            
            if win_check(Gme_list, Player2_Mrker):
                display_board(Gme_list)
                print(" Congrts Player 2 won the Game .....")
                Game_on=False
            else:
                if full_board_check(Gme_list):
                    display_board(Gme_list)
                    print(" The Match is draw .....")
                    break
                else:
                    turn='Player 1'
    if not replay():
        break