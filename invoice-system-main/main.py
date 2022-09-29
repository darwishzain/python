import Tkinter as tk #sudo apt-get install python-tk
import csv

root = tk.Tk()
root.title("Invoice System")

#canvas = tk.Canvas(root, width=600, height=600)
#canvas.grid(columnspan=5)

with open("productInfo.csv") as file_name:
    file_read = csv.reader(file_name)
    product = list(file_read)
    print(product)
    print(product[]=='1123')

newBtn = tk.Button(root,text='New', bg='#00ac9f')
newBtn.grid(row=0, column=0)
cancelBtn = tk.Button(root, text='Cancel', bg='red')
cancelBtn.grid(row=0, column=4)
okBtn = tk.Button(root, text='OK', bg='green')
okBtn.grid(row=4, column=4)

labelOrder = tk.Label(root, text='Order')
labelOrder.grid(columnspan=3, row=1, column=0)

listId = tk.Text(root, height=20, width=30)
listId.grid(columnspan=3, row=2, column=0)
listPrice = tk.Text(root, height=20, width=10)
listPrice.grid(columnspan=2, row=2, column=3)

itemId = tk.Text(root, height=2, width=20)
itemId.grid(columnspan=2, row=3, column=0)
itemPrice = tk.Text(root, height=2, width=10)
itemPrice.grid(columnspan=1, row=3, column=2)

totalPrice = tk.Text(root, height=2, width=10, bg='limegreen')
totalPrice.grid(columnspan=2, row=3, column=3)





root.mainloop()