import numpy as np
from random import randrange

n = 3
board = np.full(n*n, 0)

def PrintBoard(board):
	# print("Currently the board looks like this!")
	for i in range(0, n):
		for j in range(0, n):
			index = i*n+j
			print(board[index], end=' ')
		print( )
	print('\n')

# Checkes if the board has a winner for horizontal lines, returns 1, if p1 has won, 2 if p2 has won and 0 if no horizontal winner is there
def HorizontalWin(board):
	for i in range(0, n):
		win = (sum(board[n*i:n*i+n])) # The indices we need are from n*i to n*i+n-1 inclusive, so as the colon operator does is not inclusive, the index written is n*i to n*i+n-1+1=n*i+n
		if(win == n):
			return 1
		elif(win == -1*n):
			return 2
		else:
			return 0
# Check if there is a vertical row with the filled with the same number, 1 or -1
def VerticalWin(board):
	for i in range(0, n):
		win = 0 # For each vertical column we reset the sum to 0
		for j in range(0, n):
			win = win + board[n*j+i] # Here loop over a single column, i 
		if(win == n):
			return 1
		elif(win == -1*n):
			return 2
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
		return 2
	else:
		# Check for the second diagonal
		win = 0
		for i in range(0, n):
			win = win + board[n*i+n-1-i]
		if(win == n):
			return 1
		elif(win == -1*n):
			return 2
		else:
			return 0
def CheckBoardFull(board):
	for i in range(0, n*n):
		if(board[i]==0):
			return -1
	return 0


def CheckWin(board):
	winner = HorizontalWin(board)
	if(winner!=0):
		return winner
	winner = VerticalWin(board)
	if(winner!=0):
		return winner
	winner = DiagonalWin(board)

	full = CheckBoardFull(board)
	if(winner==0 and full==-1):
		return 0
	elif(winner==0 and full==0):
		return -3
	elif(winner!=0):
		return winner
def ComputerStrategy(board):
	# Generate a random number in a given board range
	p1_ind = randrange(n*n)
	# Re generate the random number until the space is empty
	while board[p1_ind]!=0:
		p1_ind = randrange(n*n)
	return p1_ind
# Print the behinning
print("Let us play a game of tic-tac-toe.")
# Initialiaze the winner to some random value
PrintBoard(board)
winner = 0
# Run the while loop until we have a winner and if the board is not full
while winner!=1 and winner!=2 and winner!=-3:
	# Computer strategy
	p1_ind = ComputerStrategy(board)
	# We not have a p1_ind which is set for an empyty spot
	board[p1_ind] = 1 # Set the value for player 1
	print("My turn!")
	# Print the board for visualization
	PrintBoard(board)
	# Check if we have a winner
	winner = CheckWin(board)
	if(winner==1 or winner==-3):
		break
	# Now the player2 can choose a number
	print("Now your turn to choose an integer between [0,8]")
	p2_ind = input()
	p2_ind = int(p2_ind)
	while(p2_ind<0 or p2_ind>8):
		print("Pick the correct number idiot!")
		p2_ind = input()
		p2_ind = int(p2_ind)

	# Ask user for input as long as the board position choosen is empty
	while(board[p2_ind]!=0):
		print("Oops! That position seems to be filled. Choose another one!")
		PrintBoard(board)
		p2_ind = input()
		p2_ind = int(p2_ind)
	# Set the value for board two player
	board[p2_ind] = -1
	print("The board looks like this!")
	# Print the board
	PrintBoard(board)
	# Check for winner
	winner = CheckWin(board)

if(winner == 1):
	print("Fuck you loser!")
elif(winner == 2):
	print("I accept defeat!")
else:
	print("Its a draw! Let us shake hands")

# PrintBoard(board)
# value = (CheckWin(board))
# print(value)
