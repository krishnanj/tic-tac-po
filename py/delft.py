import tkinter as tk


# def changeColor():
#     buttonB.configure(bg="yellow") 

# root = tk.Tk()
# root.geometry("250x100")
# buttonA = tk.Button(root,
#                      text = "Color",
#                      bg = "blue",
#                      fg = "red")

# buttonB = tk.Button(root,
#                     text="Click to change color",
#                     command=changeColor)
# buttonA.pack(side=tk.LEFT)
# buttonB.pack(side=tk.RIGHT)
# root.mainloop()
       

def main(self):
    root = Tk()
    frame=Frame(root)
    frame.grid(row=0,column=0)

    self.btn=  [[0 for x in xrange(20)] for x in xrange(60)] 
	for x in range(60):  
		for y in range(20):
			self.btn[x][y] = Button(frame,command= lambda x1=x, y1=y: self.color_change(x1,y1))
			self.btn[x][y].grid(column=x, row=y)

     root.mainloop()

def color_change(self,x,y):
    self.btn[x][y].config(bg="red")
    print x,y