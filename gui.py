import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

import numpy as np
import board as bd

n = 3
sz = 100
pad = 0
tc = 2
geo = '500x350'
fr = 10
board = np.full(n*n, 0)
# create a main tkinter window
root = tk.Tk()
root.title('Tic-Tac-Toe')
root.geometry(geo)


# create all of the main containers
center = tk.Frame(root, bg='white', width=fr, height=fr, padx=pad, pady=pad)

# layout all of the main containers
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)
center.grid(row=1)

cells = {}
for row in range(n):
    Grid.rowconfigure(frame, row, weight=1)
    for column in range(n):
        Grid.columnconfigure(frame, column, weight=1)
        btn = Button(frame, text='This one?')
        btn.grid(row=row, column=column, sticky=N+S+E+W)
        cell = tk.Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=tc,
                     width=sz, height=sz,  padx=pad,  pady=pad)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell
        # Grid.columnconfigure(frame, col_index, weight=1)
        # btn = Button(frame) #create a button inside frame 
        # btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
def DrawBoard(board):
    for i in range(0, n):
        for j in range(0, n):
            index = i*n+j
            if(board[index]==1):
                cells[(i,j)].configure(background="red")
            elif(board[index]==-1):
                cells[(i,j)].configure(background="blue")

def task():
    # Print the behinning
    print("Let us play a game of tic-tac-toe.")
    # Initialiaze the winner to some random value
    # bd.PrintBoard(board)
    DrawBoard(board)
    winner = 0
    # Run the while loop until we have a winner and if the board is not full
    while winner!=1 and winner!=2 and winner!=-3:
        # Computer strategy
        p1_ind = bd.ComputerStrategy(board)
        # We not have a p1_ind which is set for an empyty spot
        board[p1_ind] = 1 # Set the value for player 1
        # print("My turn!")
        # Print the board for visualization
        # bd.PrintBoard(board)
        DrawBoard(board)
        # Check if we have a winner
        winner = bd.CheckWin(board)
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
            # bd.PrintBoard(board)
            DrawBoard(board)
            p2_ind = input()
            p2_ind = int(p2_ind)
        # Set the value for board two player
        board[p2_ind] = -1
        # print("The board looks like this!")
        # Print the board
        # bd.PrintBoard(board)
        DrawBoard(board)
        # Check for winner
        winner = bd.CheckWin(board)

    if(winner == 1):
        print("Fuck you loser!")
        root.quit()
    elif(winner == 2):
        print("I accept defeat!")
        root.quit()
    else:
        print("Its a draw! Let us shake hands")
        root.quit()
    root.after(1000, task)  # reschedule event in 2 seconds

root.after(2000, task)
root.mainloop()

# board = [1,1,0,-1,0,-1,1,1,1]
# for i in range(0, n):
#     for j in range(0, n):
#         index = i*n+j
#         if(board[index]==1):
#             cells[(i,j)].configure(background="red")
#         elif(board[index]==-1):
#             cells[(i,j)].configure(background="blue")

# root.mainloop() 	#https://stackoverflow.com/questions/48027440/how-to-create-a-9x9-grid-more-efficiently-python-tkinter


