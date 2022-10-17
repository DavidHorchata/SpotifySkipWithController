from tkinter import *
from tkinter import ttk
import threading
from controller import Controller
win= Tk()

win.title("Spotify Skip")
win.geometry("350x250")


def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)


hasCredentials =  True

def on_close():

    controllerLink.flag = False

    win.destroy()

    
def startLabel():
    label=Label(win, text="Running...", font=("Veranda 22 bold"), pady="50px")
    label.configure(bg="grey")
    label.pack()
    btn.destroy()

if hasCredentials:

    #btn = Button(root, text="Click Me", command=threading.Thread(target=combine).start)
    controllerLink = Controller()
    spotifyThread = threading.Thread(target=controllerLink.startLoop, daemon=True)
    btn = ttk.Button(win, text= "Run Program",width= 20, command= lambda:[spotifyThread.start(),startLabel()])
    btn.configure()
    btn.pack(pady=20)

    


else:
    #Initialize a Label to display the User Input
    label=Label(win, text="", font=("Veranda 22 bold"))
    label.pack()

    entry= Entry(win, width= 40)
    entry.focus_set()
    entry.pack()

    ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.protocol("WM_DELETE_WINDOW",  on_close)
win.configure(bg='grey')
win.mainloop()