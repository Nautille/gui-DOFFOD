from tkinter import *
from numpy import place, size
import tkinter as tk
from setuptools import Command


app = Tk()

sideCheck = 0
Check = 0
# style of page


app.title("Main")
app.geometry("900x450")
app.resizable(0, 0)




def toggle():
    if config2.config('relief')[-1] == 'sunken':
        config2.config(relief="raised", text="ON")
    else:
        config2.config(relief="sunken", text="OFF")

def clickMe():
    label2.configure(text= 'Timer ' + nameXD.get())
 
def close_win():
    app.destroy()


on = PhotoImage(file= "C:/Users/Nauti/Documents/dofustools/doffod/bouton_activ.png")
off = PhotoImage(file= "C:/Users/Nauti/Documents/dofustools/doffod/bouton_desac.png")
quitter = PhotoImage(file = "C:/Users/Nauti/Documents/dofustools/doffod/croix.png")
bgimg = PhotoImage(file = "C:/Users/Nauti/Documents/dofustools/doffod/fenetre.png")


canvas1 = Canvas(app, width=900, height=450)
canvas1.pack()
canvas1.create_image(0, 0, image = bgimg, anchor = "nw")

label2 = Label(app, text = "Timer", bg="gray")
label2.place(x=190, y=70)

nameXD = tk.StringVar()
nameEntered = Entry(app, width = 15, textvariable = nameXD)
nameEntered.place(x=190, y=90)
 
buttonXD = Button(app, text = "Set Timer", bg="gray", command = clickMe)
buttonXD.place(x=190, y=110)

config1 = Button(
    app, image = quitter, command=close_win)
config1.place(x=870, y=0)

config2 = Button(
    app, text = "Suivis automatique", bg="gray", relief="raised", command= toggle)
config2.place(x=50, y=70)

config3 = Button(
    app, text='Paramètres Bind', bg="gray")
config3.place(x=50, y=120)

settingTimer = Button(
    app, text='Paramètres Prout', bg="gray")
settingTimer.place(x=50, y=170)

launchDOFUS = Button(
    app, text='Lancer Dofus', bg="gray")
launchDOFUS.place(x=50, y=220)



app.mainloop()