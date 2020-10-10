# import tkinter as Tk
from tkinter import *
# # import ttk

# class App(object):
#     def __init__(self, master, **kwargs):
#         master = master
#         create_text()

#     def create_text(self):
#         textbox = tk.Text(master, height = 10, width = 79, wrap = 'word')
#         vertscroll = tk.Scrollbar(master)
#         vertscroll.config(command=textbox.yview)
#         textbox.config(yscrollcommand=vertscroll.set)
#         textbox.grid(column=0, row=0)
#         vertscroll.grid(column=1, row=0, sticky='NS')

# root = tk.Tk()
# app = App(root)
# root.mainloop()
def main():
    root = Tk()
    frame=Frame(root)
    frame.grid(row=0,column=0)

    btn=  [[0 for x in range(2)] for x in range(6)] 
    for x in range(6):
        for y in range(2):
            btn[x][y] = Button(frame,command= lambda x1=x, y1=y: color_change(x1,y1))
            btn[x][y].grid(column=x, row=y)

    root.mainloop()

def color_change(self,x,y):
    btn[x][y].config(bg="red")
    print (x,y)
main()