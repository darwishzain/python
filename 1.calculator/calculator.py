from tkinter import *

calc = Tk()
calc.title("Calculator 1.0 (Beta)")
operator=""
text_Input =StringVar()

def btnClick (numbers) :
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear() :
    global operator
    operator = ""
    text_Input.set("")

def btnEqual() :
    global operator
    sumup = str(eval (operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(calc,font=('arial',20,'bold'), textvariable=text_Input, bd=20, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

##Number Buttons
btn7 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="7", command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="8", command=lambda:btnClick(8) ).grid(row=1,column=1)
btn9 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="9", command=lambda:btnClick(9) ).grid(row=1,column=2)
btn4 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="4", command=lambda:btnClick(4) ).grid(row=2,column=0)
btn5 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="5", command=lambda:btnClick(5) ).grid(row=2,column=1)
btn6 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="6", command=lambda:btnClick(6) ).grid(row=2,column=2)
btn3 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="1", command=lambda:btnClick(1) ).grid(row=3,column=0)
btn2 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="2", command=lambda:btnClick(2) ).grid(row=3,column=1)
btn1 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="3", command=lambda:btnClick(3) ).grid(row=3,column=2)
btn0 = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="0", command=lambda:btnClick(0) ).grid(row=4,column=0)

equal = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="=", command=btnEqual).grid(row=4, column=1)
clear = Button (calc, padx=16, bd=8, fg="black", font = ('arial', 20, 'bold'), text="C", command=btnClear).grid(row=4, column=2)

##Arithmetic Function
multiply = Button (calc, padx=16, bd=8, fg="white", bg="black", font = ('arial', 20, 'bold'), text="*", command=lambda:btnClick("*")).grid(row=1, column=3)
divide =   Button (calc, padx=16, bd=8, fg="white", bg="black", font = ('arial', 20, 'bold'), text="/", command=lambda:btnClick("/")).grid(row=2, column=3)
plus =     Button (calc, padx=16, bd=8, fg="white", bg="black", font = ('arial', 20, 'bold'), text="+", command=lambda:btnClick("+")).grid(row=3, column=3)
minus =    Button (calc, padx=16, bd=8, fg="white", bg="black", font = ('arial', 20, 'bold'), text="-", command=lambda:btnClick("-")).grid(row=4, column=3)

##Copyright
myLabel = Label (calc, text="Copyright Reserved Darwish Zain Studio 2020", font=('arial', 10, 'bold')).grid(columnspan=4)

calc.mainloop()
