import Tkinter as tk
import time

root = tk.Tk()
root.title('Basic')

global operator
operator=""
textInput = tk.StringVar()

def btnClick(number):
    global operator
    operator = operator + str(number)
    textInput.set(operator)

def btnClear():
    global operator
    operator = ""
    textInput.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    textInput.set(sumup)
    operator=""

mainFrame = tk.Frame(root, bd=1)
mainFrame.grid()
txtDisplay = tk.Entry(mainFrame,textvariable=textInput, bd=0,width=40, bg="#f0f0f0", justify='right', insertwidth=4)
txtDisplay.grid(row=0, column=0,columnspan=5)
# ! as
############Numbers############
###number Row1
btn7 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="7", command=lambda: btnClick(7))
btn7.grid(row=1, column=0)
btn8 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="8", command=lambda: btnClick(8))
btn8.grid(row=1, column=1)
btn9 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="9", command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
###number Row2
btn4 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="4", command=lambda: btnClick(4))
btn4.grid(row=2, column=0)
btn5 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="5", command=lambda: btnClick(5))
btn5.grid(row=2, column=1)
btn6 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="6", command=lambda: btnClick(6))
btn6.grid(row=2, column=2)
###number Row3
btn1 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="1", command=lambda: btnClick(1))
btn1.grid(row=3, column=0)
btn2 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="2", command=lambda: btnClick(2))
btn2.grid(row=3, column=1)
btn3 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="3", command=lambda: btnClick(3))
btn3.grid(row=3, column=2)
###Row4
btn0 = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="0", command=lambda: btnClick(0))
btn0.grid(row=4, column=0)
btnd = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text=".", command=lambda: btnClick("."))
btnd.grid(row=4, column=1)

############Calc############
btnMul = tk.Button(mainFrame, width=5,bg='#f0f0f0', fg='#000000', text="*", command=lambda: btnClick("*"))
btnMul.grid(row=2, column=3)
btnDiv = tk.Button(mainFrame, width=5,bg='#f0f0f0', fg='#000000', text="/", command=lambda: btnClick("/"))
btnDiv.grid(row=2, column=4)
btnAdd = tk.Button(mainFrame, width=5,bg='#f0f0f0', fg='#000000', text="+", command=lambda: btnClick("+"))
btnAdd.grid(row=3, column=3)
btnMin = tk.Button(mainFrame, width=5,bg='#f0f0f0', fg='#000000', text="-", command=lambda: btnClick("-"))
btnMin.grid(row=3, column=4)

############Opt############
btnEql = tk.Button(mainFrame, width=10, bg='#f0f0f0', fg='#000000', text="=", command=btnEqual)
btnEql.grid(row=4, column=3, columnspan=2)
btnClr = tk.Button(mainFrame, width=5, bg='#f0f0f0', fg='#000000', text="C", command=btnClear)
btnClr.grid(row=1, column=4)

year = time.strftime("%Y")
copy = tk.Label(mainFrame, text="2018-"+year+"Developed by Darwish Zain")
copy.grid(columnspan=5)



root.mainloop()