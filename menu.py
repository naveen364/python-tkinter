from tkinter import *
def work():
    print("this is working")
root=Tk()
root.geometry("800x600")
menu1=Menu(root)
root.config(menu=menu1)
submenu1=Menu(menu1)
menu1.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="new project",command=work)
submenu1.add_command(label="save")
submenu1.add_command(label="save as")
submenu1.add_command(label="exit",command=quit)

submenu2=Menu(menu1)
menu1.add_cascade(label="edit",menu=submenu2)
submenu2.add_command(label="undo")
submenu2.add_command(label="redo")
submenu2.add_command(label="cut")
submenu2.add_command(label="copy")
submenu2.add_command(label="past")                     

submenu3=Menu(menu1)
menu1.add_cascade(label="help",menu=submenu3)
submenu3.add_command(label="about IDLE")
submenu3.add_command(label="idle help")
submenu3.add_command(label="python docs")

root.mainloop()

