from tkinter import *

class thisSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x260")
        self.root.configure(background="black")
        self.root.iconbitmap('./icon.ico')

        global operator
        operator=""
        text_Input=StringVar()

        def btnClick(numbers) :
            global operator
            operator = operator + str(numbers)
            text_Input.set(operator)

        def btnClear() :
            global operator
            operator=""
            text_Input.set("")

        def btnEqual() :
            global operator
            sumup = str(eval (operator))
            text_Input.set(sumup)
            operator=""


        mainFrame = Frame(self.root, bd=1, width=256, height=380,bg="white", relief = RIDGE)
        mainFrame.grid()
        txtDisplay = Entry(mainFrame,textvariable=text_Input, bd=1, width=45, bg="powder blue", justify='right', insertwidth=4)
        txtDisplay.grid(columnspan=4)

        ############Numbers############
        ###Row1
        btn7 = Button(mainFrame, padx=32, pady=16, fg='black', text="7", command=lambda: btnClick(7)).grid(row=1, column=0)
        btn8 = Button(mainFrame, padx=32, pady=16, fg='black', text="8", command=lambda: btnClick(8)).grid(row=1, column=1)
        btn9 = Button(mainFrame, padx=32, pady=16, fg='black', text="9", command=lambda: btnClick(9)).grid(row=1, column=2)
        ###Row2
        btn4 = Button(mainFrame, padx=32, pady=16, fg='black', text="4", command=lambda: btnClick(4)).grid(row=2, column=0)
        btn5 = Button(mainFrame, padx=32, pady=16, fg='black', text="5", command=lambda: btnClick(5)).grid(row=2, column=1)
        btn6 = Button(mainFrame, padx=32, pady=16, fg='black', text="6", command=lambda: btnClick(6)).grid(row=2, column=2)
        ###Row3
        btn1 = Button(mainFrame, padx=32, pady=16, fg='black', text="1", command=lambda: btnClick(1)).grid(row=3, column=0)
        btn2 = Button(mainFrame, padx=32, pady=16, fg='black', text="2", command=lambda: btnClick(2)).grid(row=3, column=1)
        btn3 = Button(mainFrame, padx=32, pady=16, fg='black', text="3", command=lambda: btnClick(3)).grid(row=3, column=2)
        ###Row4
        btn0 = Button(mainFrame, padx=32, pady=16, fg='black', text="0", command=lambda: btnClick(0)).grid(row=4, column=0)

        ############Calc############
        btnMul = Button(mainFrame, padx=32, pady=16,fg='black', text="*", command=lambda: btnClick("*")).grid(row=1, column=3)
        btnAdd = Button(mainFrame, padx=32, pady=16,fg='black', text="+", command=lambda: btnClick("+")).grid(row=2, column=3)
        btnMin = Button(mainFrame, padx=32, pady=16,fg='black', text="-", command=lambda: btnClick("-")).grid(row=3, column=3)
        btnDiv = Button(mainFrame, padx=32, pady=16,fg='black', text="/", command=lambda: btnClick("/")).grid(row=4, column=3)

        ############Opt############
        btnEql = Button(mainFrame, padx=32, pady=16, fg='black', text="=", command=btnEqual).grid(row=4, column=1)
        btnClr = Button(mainFrame, padx=32, pady=16, fg='black', text="C", command=btnClear).grid(row=4, column=2)

        Label(mainFrame, text="2020 Copyright Reserved. Darwish Zain Studio").grid(columnspan=4)




if __name__ == '__main__':
    root=Tk()
    application=thisSystem(root)
    root.mainloop()
