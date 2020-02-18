import os
import time
import random

def clear_screen():
	os.system('cls')

def display_board(board):
	clear_screen()
	vertical_elements = '   |   |   '
	horizontal_elements = '-----------'
	line3 = ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' '
	line2 = ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' '
	line1 = ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' '
	print(vertical_elements)
	print(line3)
	print(vertical_elements)
	print(horizontal_elements)
	print(vertical_elements)
	print(line2)
	print(vertical_elements)
	print(horizontal_elements)
	print(vertical_elements)
	print(line1)
	print(vertical_elements)

def player_input():
	'''
	OUTPUT = (Player 1 marker, Player 2 marker)
	'''
	mark = ''
	while mark != 'X' and mark != 'O':
		mark = input('Player 1: choose X or O: ').upper()
	if mark == 'X':
		return ('X','O')
	else:
		return ('O','X')

def place_marker(board, mark, position):
	board[position] = mark

def win_check(board, mark):
	return ((board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[1] == board[4] == board[7] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	(board[1] == board[5] == board[9] == mark) or
	(board[3] == board[5] == board[7] == mark))

start_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(start_board)
player_1_marker, player_2_marker = player_input()

board_position = int(input("Please enter a number for the board position choice: "))

place_marker(start_board,  ,board_position)
display_board(start_board)
'''time.sleep(3)
clear_screen()'''


