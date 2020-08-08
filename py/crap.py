from tkinter import *
import tkinter as tk
from functools import partial

n = 3
sz = 300
pad = 3
tc = 2
geo = '100x100'
fr = 10


#Create & Configure root 
root = Tk()
# Grid.rowconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 0, weight=1)

# center = tk.Frame(root, bg='white', width=fr, height=fr, padx=pad, pady=pad)

# def my_func_name(sequence, index):
#     widget = sequence[index]
#     widget.configure(bg='blue') #  for example

#Create & Configure frame 
# frame=Frame(root)
# frame.grid(row=0, column=0, sticky=N+S+E+W)

def callback(r,c, butmat):
    print(r,c)
    butmat[r][c].configure(text = '1', bg='red')


cells = {}
butmat = [[0 for x in range(n)] for x in range(n)]
#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(n):
    # Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(n):
        # Grid.columnconfigure(frame, col_index, weight=1)
        # btn = Button(frame, text = 'text', command=callback) #create a button inside frame 
        # btn.grid(row=row_index, column=col_index, sticky=N+S+E+W) 
        # cell = tk.Frame(center, bg='white', highlightbackground="black",
        #              highlightcolor="black", highlightthickness=tc,
        #              width=sz, height=sz,  padx=pad,  pady=pad)
        # cell.grid(row=row_index, column=col_index)
        # cells[(row_index, col_index)] = cell
        # i = 0
        # j = 1 
        # par = partial(my_func_name, btn, 1)
        butmat[row_index][col_index] = Button(root,command=partial(callback,row_index, col_index,butmat), padx=25, pady=25, bg = "#66CCCC",highlightcolor='red')
        butmat[row_index][col_index].grid(row=row_index, column=col_index)
        # but.config(bg='red')


# cells[(0,1)].configure(background="red")


root.mainloop()