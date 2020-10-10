import numpy as np
from random import randrange

## adding gui stuff
from tkinter import *
from functools import partial

n = 3
mode = 'human' # human

root = Tk()

def Array2Grid(index):
    a = index%n
    b = int(np.floor(index/n))
    if(n*b+a != index):
        print("Something strange!")
    return a, b

def Grid2Array(r, c):
    index = r*n+c
    return index

def callback(r,c, butmat):
    p2_ind = Grid2Array(r, c)
    butmat[r][c].configure(text = '1', bg='red', highlightbackground='blue')

# prints a 3 by 3 matrix board
def PrintBoard(board):
	# print("Currently the board looks like this!")
	for i in range(0, n):
		for j in range(0, n):
			index = i*n+j
			print(board[index], end=' ')
		print( )
	print('\n')

# Checks if the board has a winner for horizontal lines, returns 1 if p1 has won (counts 1), 2 if p2 has won (counts -1) and 0 if no horizontal winner is there
def HorizontalWin(board):
	for i in range(0, n):
		win = (sum(board[n*i:n*i+n])) # The indices we need are from n*i to n*i+n-1 inclusive, so as the colon operator does is not inclusive, the index written is n*i to n*i+n-1+1=n*i+n
		if(win == n):
			return 1		# if player 1 wins
		elif(win == -1*n):
			return -1		# if player 2 wins
	return 0		# if the game is draw


# Check if there is a vertical row with the filled with the same number, 1 or -1
def VerticalWin(board):
	for i in range(0, n):
		win = 0 # For each vertical column we reset the sum to 0
		for j in range(0, n):
			win = win + board[n*j+i] # Here loop over a single column, i 
		if(win == n):
			return 1
		elif(win == -1*n):
			return -1
	return 0 # If we have not returned earlier then this should be the case 

# Check if either of the diagonals are filled with -1 or 1
def DiagonalWin(board):
	# Check for the main diagonal
	win = 0
	for i in range(0, n):
		win = win + board[n*i+i]
	if(win == n):
		return 1
	elif(win == -1*n):
		return -1
	else:
		# Check for the second diagonal
		win = 0
		for i in range(0, n):
			win = win + board[n*i+n-1-i]
		if(win == n):
			return 1
		elif(win == -1*n):
			return -1
		else:
			return 0

# checks if the board is full of 1 and -1 or not. If full, returns True else returns False
def CheckBoardIsFull(board):
	for i in range(0, n*n):
		if(board[i]==0):
			return False
	return True

# finds who wins the game at every step or if the board is full
def CheckWin(board):
	PrintBoard(board)
	# if there exists no winner currently along the vertical
	winner = VerticalWin(board)
	print("Vertical win: ",winner)
	if(winner!=0):
		return winner

	# checks for horizontal, vertical and diagonal wins if there is no draw
	# each of these wins are evaluated independently
	winner = HorizontalWin(board)
	print("Horizontal win: ",winner)
	# if there exists no winner currently along the horizontal
	if(winner!=0):
		return winner


	# if there exists winner currently along the diagonal
	winner = DiagonalWin(board)
	print("Diagonal win: ",winner)
	if(winner!=0):
		return winner

	# check if the complete board is full, then return draw game
	full = CheckBoardIsFull(board)

	# if the game is not yet won and the board is full, then returns -2 (game ends in a draw)
	if(full):
		return -2
	# there is no winner and the board is not full, then return 0 (game continues) 
	else:
		return 0

## player 1 is computer and it picks random numbers to play
def ComputerStrategy(board):
	# p1 is computer; Generate a random number in a given board range
	p1_ind = randrange(n*n)
	# Re generate the random number until the space is empty
	while board[p1_ind]!=0:
		p1_ind = randrange(n*n)
	return p1_ind

# Print the beginning
print("Let us play a game of tic-tac-toe.")

# Initialiaze the winner to some random value
board = np.full(n*n, 0)
# PrintBoard(board)
winner = 0
count = 0
# Run the while loop until we have a winner and if the board is not full
# winner =1, player 1 wins; -1, player 2; -2, draw
while winner!=1 and winner!=-1 and winner!=-2:
	print("Round: ", count)
	count = count + 1
	# Computer strategy
	p1_ind = ComputerStrategy(board)

	# We not have a p1_ind which is set for an empty spot
	board[p1_ind] = 1 # Set the value for player 1
	# print("My turn!")

	# Print the board for visualization
	# PrintBoard(board)

	# Check if we have a winner
	winner = CheckWin(board)
	# print(winner)
	if(winner==1 or winner==-2):
		break

	if (mode == 'human'):

	# Now the player2 can choose a number
		print("Now your turn to choose an integer between [1,9]")
		p2_ind = input()
		p2_ind = int(p2_ind)
		while(p2_ind<1 or p2_ind>9):
			print("Pick the correct number idiot!")
			p2_ind = input()
			p2_ind = int(p2_ind)

		# Ask user for input as long as the board position chosen is empty
		while(board[p2_ind-1]!=0):
			print("Oops! That position seems to be filled. Choose another one!")
			p2_ind = input()
			p2_ind = int(p2_ind)

		# Set the value for board two player
		board[p2_ind-1] = -1
		print("The board looks like this!")

	else:

		p2_ind = ComputerStrategy(board)

		# Set the value for board two player
		board[p2_ind] = -1
		# print("The board looks like this!")

	# Print the board
	# PrintBoard(board)

	# Check for winner
	winner = CheckWin(board)

	# print('Final', winner!=1 and winner!=-1 and winner!=-2)


PrintBoard(board)
value = (CheckWin(board))
print(value)

# if(winner == 1):
# 	print("Fuck you loser!")
# elif(winner == -1):
# 	print("I accept defeat!")
# else:
# 	print("Its a draw! Let us shake hands")

