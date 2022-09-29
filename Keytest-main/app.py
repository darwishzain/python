import tkinter as tk
from pynput import keyboard

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Keyboard Test V1.0')
        self.master.geometry("600x400")
        self.master.configure(background="white")
        #self.master.iconbitmap('./icon.ico')
        self.pack()
        self.start()

    def start(self):
        self.frameLabel = tk.Label(self)
        self.frameLabel["text"] = "Keyboard Test by Darwish Zain Studio"
        self.frameLabel.grid(row=0,columnspan=10)

        self.frame = tk.Frame(self)
        self.frame.grid(row=3)

        ###Keyboard Row 3
        self.q = tk.Label(self.frame, padx=20, pady=5, text='q').grid(column=0,row=1)
        self.w = tk.Label(self.frame, padx=20, pady=5, text='w').grid(column=1,row=1)
        self.e = tk.Label(self.frame, padx=20, pady=5, text='e').grid(column=2,row=1)
        self.r = tk.Label(self.frame, padx=20, pady=5, text='r').grid(column=3,row=1)
        self.t = tk.Label(self.frame, padx=20, pady=5, text='t').grid(column=4,row=1)
        self.y = tk.Label(self.frame, padx=20, pady=5, text='y').grid(column=5,row=1)
        self.u = tk.Label(self.frame, padx=20, pady=5, text='u').grid(column=6,row=1)
        self.i = tk.Label(self.frame, padx=20, pady=5, text='i').grid(column=7,row=1)
        self.o = tk.Label(self.frame, padx=20, pady=5, text='o').grid(column=8,row=1)
        self.p = tk.Label(self.frame, padx=20, pady=5, text='p').grid(column=9,row=1)
        
        ###Keyboard Row 2

    def keypressed(key):
        print('Key {0}'.format(key))
        if key == Key.delete:
            return False
        if key == Key.space:
            self.u['bg']='green'
            return False

    with keyboard.Listener(on_press = keypressed) as listener:
        listener.join()
    


root = tk.Tk()
app = Application(master=root)
app.mainloop()