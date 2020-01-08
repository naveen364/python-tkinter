from tkinter import *
root=Tk()
root.geometry("800x600")

def left(event):
    print("left click")

def middle(event):
    print("middle click")

def right(event):
    print("right click")

frame=Frame(root,width=400,height=300)
frame.bind("<Button-1>",left)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",right)
frame.pack()

root.mainloop()
