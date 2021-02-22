from tkinter import *
from tkinter import messagebox

top = Tk()
L1 = Label(top,text="UserName")
L1.grid(column=0,row=0)

E1=Entry(top,bd=5)
E1.grid(column=1, row=0)

E2=Entry(top,bd=5)
E2.grid(column=2,row=0)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 4
newmsg = ''

def submit():

    messagebox.showinfo("CONFIRMATION", E1.get()+"- Your Data")
    global newmsg
    for Character in E1.get():  # ab

        position = alphabet.find(Character)         # Position    = 1, 2
        newposition = (position + key) % 26         # NewPosition = 1+4%26=5, 2+4%26=6
        newchar = alphabet[newposition]             # alphabet[5] = e, f
        print('Encrypted new character is', newchar)
        newmsg += newchar
    print(newmsg)
    E2.insert(0, newmsg)
redbutton=Button(top,text="Viswa Button",fg="red", command=submit)
redbutton.grid(column=1, row=1)
top.mainloop()