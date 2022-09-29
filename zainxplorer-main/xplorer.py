from tkinter import *
import os
import sys
from win32api import GetSystemMetrics
#import tkMessageBox

xplorer = Tk()
###make window fit to screen...
screenWidth = str(GetSystemMetrics(0))#get screen resolution(width) -> into string
screenHeight = str(GetSystemMetrics(1))#get screen resolution(height) -> into string
#because geometry don't accept integer

xplorer.title("Zain Xplorer")
xplorer.geometry(screenWidth+"x"+screenHeight)#widthxheight
xplorer.configure(bg="white")

#theLocation = Label(xplorer, text="Welcome to Zain Xplorer").grid(row=0, column=0, padx=50)
topPanel = PanedWindow(xplorer, width=screenWidth, height='100px').pack(padx=5, pady=10, side=TOP)
leftPanel = PanedWindow(xplorer, background="blue", width='250px',height='400px').pack(padx=5, pady=10, side=LEFT)
centerPanel = PanedWindow(xplorer, background='green', width="500px", height='400px').pack(padx=5, pady=10, side=LEFT)
rightPanel = PanedWindow(xplorer, background='red', width='200px', height='400px').pack(padx=5, pady=10, side=LEFT)
startBtn = Button(leftPanel, text="Start").pack()

drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]
for i in range(len(drives)):
    Button(xplorer, text=drives[i]).pack(side=LEFT)
    print(drives[i])

#print(drives)
#theText = Text(centerPanel).pack()



xplorer.mainloop()
