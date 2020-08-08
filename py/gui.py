import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

n = 3
sz = 300
pad = 3
tc = 2
geo = '100x100'
fr = 10

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
	# Grid.rowconfigure(frame, row_index, weight=1)
    for column in range(n):
        cell = tk.Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=tc,
                     width=sz, height=sz,  padx=pad,  pady=pad)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell
        # Grid.columnconfigure(frame, col_index, weight=1)
        # btn = Button(frame) #create a button inside frame 
        # btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  


cells[(0,1)].configure(background="red")



root.mainloop() 	#https://stackoverflow.com/questions/48027440/how-to-create-a-9x9-grid-more-efficiently-python-tkinter

