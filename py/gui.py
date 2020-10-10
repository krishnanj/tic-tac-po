from tkinter import *
import tkinter as tk
from functools import partial
import numpy as np
import board as bd

import time

n = 3
sz = 100
pad = 0
tc = 2
# geo = '500x350'
geo = '100x100'
fr = 10
board = np.full(n*n, 0)
# create a main tkinter window
root = tk.Tk()
# root.title('Tic-Tac-Toe')
# root.geometry(geo)


# # create all of the main containers
# center = tk.Frame(root, bg='white', width=fr, height=fr, padx=pad, pady=pad)

# # layout all of the main containers
# Grid.rowconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 0, weight=1)
# # root.grid_rowconfigure(0, weight=1)
# # root.grid_columnconfigure(0, weight=1)
# frame=Frame(root)
# frame.grid(row=0, column=0, sticky=N+S+E+W)
# center.grid(row=1)

# cells = {}
# for row in range(n):
#     Grid.rowconfigure(frame, row, weight=1)
#     for column in range(n):
#         Grid.columnconfigure(frame, column, weight=1)
#         btn = Button(frame, text='This one?')
#         btn.grid(row=row, column=column, sticky=N+S+E+W)
#         cell = tk.Frame(center, bg='white', highlightbackground="black",
#                      highlightcolor="black", highlightthickness=tc,
#                      width=sz, height=sz,  padx=pad,  pady=pad)
#         cell.grid(row=row, column=column)
#         cells[(row, column)] = cell
        # Grid.columnconfigure(frame, col_index, weight=1)
        # btn = Button(frame) #create a button inside frame 
        # btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
# def callback(r,c, butmat, p):
#     if(p=='comp'):
#         butmat[r][c].configure(text = '1', bg='red', highlightbackground='red')
#     elif(p=='hum'):
#         butmat[r][c].configure(text = '-1', bg='green', highlightbackground='green')
#         print(r, c)
#     return r, c
def Array2Grid(index):
    a = index%n
    b = int(np.floor(index/n))
    if(n*b+a != index):
        print("Something strange!")
    return a, b

def Grid2Array(r, c):
    index = r*n+c
    return index

def HumanCallBack(rh, ch, butmat):
    butmat[rh][ch].configure(text = '-1', bg='green', highlightbackground='green')
    index = Grid2Array(rh, ch)
    board[index] = -1


def CompCallBack(rc, cc, butmat):
    butmat[rc][cc].configure(text = '1', bg='red', highlightbackground='red')
    index = Grid2Array(rc, cc)
    board[index] = 1
butmat = [[0 for x in range(n)] for x in range(n)]

#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(n):
    # Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(n):
        butmat[row_index][col_index] = Button(root,command=partial(HumanCallBack,row_index, col_index,butmat), padx=25, pady=25, bg = "#66CCCC", highlightbackground='#66CCCC')
        butmat[row_index][col_index].grid(row=row_index, column=col_index)

def DrawBoard(board):
    for i in range(0, n):
        for j in range(0, n):
            index = i*n+j
            if(board[index]==1):
                # butmat[i][j].configure(text = '1', bg='red')
                butmat[i][j] = Button(root,command=partial(callback,row_index, col_index,butmat, 'comp'), padx=25, pady=25, bg = "red",highlightcolor='red')
            elif(board[index]==-1):
                butmat[i][j] = Button(root,command=partial(callback,row_index, col_index,butmat, 'hum'), padx=25, pady=25, bg = "red",highlightcolor='red')
# def UserChoice():
#     # p2_ind = callback(r, c, butmat)
#     p2_ind = 
#     return p2_ind

# Set the value for board two player
def task():
    # Print the behinning
    print("Let us play a game of tic-tac-toe.")
    # Initialiaze the winner to some random value
    # bd.PrintBoard(board)
    winner = 0
    # Run the while loop until we have a winner and if the board is not full
    while winner!=1 and winner!=2 and winner!=-3:
        # Computer strategy
        p1_ind = bd.ComputerStrategy(board)
        rc, uc = Array2Grid(p1_ind)
        CompCallBack(rc, uc, butmat)
        # print("My turn!")
        # Print the board for visualization
        # bd.PrintBoard(board)
        # DrawBoard(board)
        # Check if we have a winner
        winner = bd.CheckWin(board)
        if(winner==1 or winner==-3):
            break
        # Now the player2 can choose a number
        print("Now your turn to choose an integer between [0,8]")
        # time.sleep(60)
        # ru, cu = callback(r,c, butmat, 2)
        # p2_ind = ru*n+cu
        # board[p2_ind] = -1
        # print("The board looks like this!")
        # Print the board
        # bd.PrintBoard(board)
        # DrawBoard(board)
        # Check for winner
        winner = bd.CheckWin(board)

    if(winner == 1):
        print("Fuck you loser!")
        # root.quit()
    elif(winner == 2):
        print("I accept defeat!")
        # root.quit()
    else:
        print("Its a draw! Let us shake hands")
        # root.quit()
    root.after(1000, task)  # reschedule event in 2 seconds
# board = [0,0,0,0,0,0,0,0,0]
# def task():
#     p1_ind = bd.ComputerStrategy(board)
#     rc, uc = Array2Grid(p1_ind)
#     CompCallBack(rc, uc, butmat)
#     root.after(1000, task)  # reschedule event in 2 seconds
# root.after(2000, task)
# rc = 0
# uc = 0
# rh, ch = callback(rc, uc, butmat, 'hum')
# print(rh, ch)
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


