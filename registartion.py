from tkinter import *
import tkinter.messagebox
import time
import os
login_id = Tk()

login_id.geometry("1600x800+0+0")

login_id.title("REGISTRATION FORM")

login_id.configure(bg='black')




#Label(login_id, text="",font=('arial',40),fg='red',bg='black').pack()
Label(login_id,font=("arial",20,"bold"),fg='red',bg='black' ,text="REGISTRATION FORM").place(x=350,y=50)
#Label(login_id, text="",font=('arial',40),fg='red',bg='black').grid(row=2,column=3)


Label(login_id, text="FIRST NAME",font=('arial',20,"bold"),fg='red',bg='black').place(x=250,y=150)
entry_1 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_1.place(x=470,y=150)
Label(login_id, text="LAST NAME",font=('arial',20,"bold"),fg='red', bg='black').place(x=250,y=200)
entry_2 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_2.place(x=470,y=200)
Label(login_id, text="USER NAME",font=('arial',20,"bold"),fg='red',bg='black').place(x=250,y=250)
entry_3 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_3.place(x=470,y=250)
Label(login_id, text="EMAIL ID",font=('arial',20,"bold"),fg='red', bg='black').place(x=250,y=300)
entry_4 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_4.place(x=470,y=300)
Label(login_id, text="GENDER",font=('arial',20,"bold"),fg='red', bg='black').place(x=250,y=350)
entry_5 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_5.place(x=470,y=350)
Label(login_id, text="AADHAR CARD",font=('arial',20,"bold"),fg='red', bg='black').place(x=250,y=400)
entry_6 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_6.place(x=470,y=400)
Label(login_id, text="PASSWORD",font=('arial',20,"bold"),fg='red', bg='black').place(x=250,y=450)
entry_7 = Entry(login_id, font=('arial',20),bg='black',fg='red')
entry_7.place(x=470,y=450)

def printMsg():
    if((entry_1.get()=='Kaushal' and entry_2.get()=='844') or (entry_1.get()=='Ks' and entry_2.get()=='744') or (entry_1.get()=='Tiger' and entry_2.get()=='944') ):
        tkinter.messagebox.showinfo('login result', 'CONGRATULATIONS!! LOGIN SUCCESSFUL')
        createWindow()
    else:
        tkinter.messagebox.showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

button_1 = Button(login_id, text="LOGIN",font=('arial',20),bg='black',fg='red', command=printMsg).place(x=400,y=550)
button_2 = Button(login_id, text="QUIT",font=('arial',20),bg='black',fg='red', command=login_id.destroy).place(x=550,y=550)


login_id.mainloop()
