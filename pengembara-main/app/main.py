from tkinter import *
import os

root = Tk()
root.title('Pengembara')

topbar = Frame(root)
topbar.grid(row=0, column=0, columnspan=3)
leftpane = Frame(root)
leftpane.grid(row=1, column=0)
centerpane = Frame(root)
centerpane.grid(row=1, column=1)
rightpane = Frame(root)
rightpane.grid(row=1, column=2)
bottombar = Frame(root)
bottombar.grid(row=2, column=0, columnspan=3)

filecount = 0

def openfile(dir):
    global filecount
    files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    Label(leftpane, text="Where").grid(row=0, column=0)
    Label(rightpane, text="Details").grid(row=0, column=0)
    for f in files:
        filecount+=1
        Label(centerpane, text=f).grid(row=filecount, column=1)

Button(topbar, text="Up", command=lambda:openfile('..')).grid(row=0, column=0)
Label(topbar, text=str(os.getcwd())).grid(row=0, column=1)

openfile('.')
Label(bottombar, text=str(filecount)+" Files").grid(row=0, column=1)

root.mainloop()