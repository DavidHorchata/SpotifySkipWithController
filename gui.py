from tkinter import *
from tkinter import ttk
import threading
from controller import Controller

import customtkinter



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
win= customtkinter.CTk()

win.title("Spotify Skip")
win.geometry("250x180")


def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)


hasCredentials =  False

def on_close():
    try:
        controllerLink.flag = False

        win.destroy()
    except:
        win.destroy()

    
def startLabel():
    label=customtkinter.CTkLabel(win, text="Running...",pady="50px")
    label.configure(font=(24))
    label.pack()
    btn.destroy()



controllerLink = Controller()
if hasCredentials:


    spotifyThread = threading.Thread(target=controllerLink.startLoop, daemon=True)
    btn = customtkinter.CTkButton(win, text= "Run Program",width= 200, height=100,command= lambda:[spotifyThread.start(),startLabel()])
    btn.pack(pady=20)

    


else:
    #Initialize a Label to display the User Input
    label2=customtkinter.CTkLabel(win, text="Accept oath for credentials",pady="50px")

    label2.pack()




win.protocol("WM_DELETE_WINDOW",  on_close)


win.mainloop()