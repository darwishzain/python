from tkinter import *
from pynput import *

class window:
    def __init__(self,root):
        self.root=root
        self.root.title("Keyboard Test")
        self.root.geometry("500x260")
        self.root.configure(background="white")
        #self.root.iconbitmap('./icon.ico') #for when we have an icon to show

        mainFrame = Frame(self.root, bd=1, width=256, height=380,bg="white", relief = RIDGE)
        mainFrame.grid()
        
        qLbl = Label(mainFrame, padx=20, pady=5, text='q').grid(column=0,row=1)
        wLbl = Label(mainFrame, padx=20, pady=5, text='w').grid(column=1,row=1)
        eLbl = Label(mainFrame, padx=20, pady=5, text='e').grid(column=2,row=1)
        rLbl = Label(mainFrame, padx=20, pady=5, text='r').grid(column=3,row=1)
        tLbl = Label(mainFrame, padx=20, pady=5, text='t').grid(column=4,row=1)
        yLbl = Label(mainFrame, padx=20, pady=5, text='y').grid(column=5,row=1)
        uLbl = Label(mainFrame, padx=20, pady=5, text='u').grid(column=6,row=1)
        iLbl = Label(mainFrame, padx=20, pady=5, text='i').grid(column=7,row=1)
        oLbl = Label(mainFrame, padx=20, pady=5, text='o').grid(column=8,row=1)
        pLbl = Label(mainFrame, padx=20, pady=5, text='p').grid(column=9,row=1)

        def on_press(key):
            try:
                theKey = format(key.char)
                print(uLbl.config)
                print(theKey)
                #if Label['text'] == theKey:
                #    print("Yesy")    
             
                
                #print('alphanumeric key {0} pressed'.format(key.char))
            except AttributeError:
                print('special key {0} pressed'.format(key))

        def on_release(key):
            print('{0} released'.format(key))
            if key == keyboard.Key.esc:
                # Stop listener
                return False

        listener = keyboard.Listener(on_press=on_press,on_release=on_release)
        listener.start()


if __name__ == '__main__':
    root=Tk()
    application=window(root)
    root.mainloop()
