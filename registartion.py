from tkinter import *
import tkinter.messagebox
import time
import os
from hoverfunc import changeOnHover

login_id = Tk()

login_id.geometry("1600x800+0+0")

login_id.title("REGISTRATION FORM")

login_id.configure(bg='orange')




#Label(login_id, text="",font=('arial',40),fg='red',bg='orange').pack()
Label(login_id,font=("arial",20,"bold","underline"),fg='red',bg='orange' ,text="REGISTRATION FORM").place(x=350,y=50)
#Label(login_id, text="",font=('arial',40),fg='red',bg='orange').grid(row=2,column=3)

###########################################################################################################################

Label(login_id, text="FIRST NAME",font=('arial',15,"bold"),fg='red',bg='orange').place(x=50,y=150)
entry_1 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_1.place(x=250,y=150)
Label(login_id, text="LAST NAME",font=('arial',15,"bold"),fg='red', bg='orange').place(x=50,y=200)
entry_2 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_2.place(x=250,y=200)
Label(login_id, text="USER NAME",font=('arial',15,"bold"),fg='red',bg='orange').place(x=50,y=250)
entry_3 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_3.place(x=250,y=250)
Label(login_id, text="DATE OF BIRTH",font=('arial',15,"bold"),fg='red', bg='orange').place(x=50,y=300)
entry_4 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_4.place(x=250,y=300)
Label(login_id, text="GENDER",font=('arial',15,"bold"),fg='red', bg='orange').place(x=50,y=350)
entry_5 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_5.place(x=250,y=350)
Label(login_id, text="AADHAR CARD",font=('arial',15,"bold"),fg='red', bg='orange').place(x=50,y=400)
button_3 = Button(login_id, text="UPLOAD",font=('arial',15,'bold'),bg='orange',fg='red')
button_3.place(x=250,y=396)
Label(login_id, text="DRIVING LICENSE",font=('arial',15,"bold"),fg='red', bg='orange').place(x=50,y=450)
button_4 = Button(login_id, text="UPLOAD",font=('arial',15,'bold'),bg='orange',fg='red')
button_4.place(x=250,y=446)

###########################################################################################################################
Label(login_id, text="PAN CARD",font=('arial',15,"bold"),fg='red',bg='orange').place(x=550,y=150)
button_5 = Button(login_id, text="UPLOAD",font=('arial',15,'bold'),bg='orange',fg='red')
button_5.place(x=700,y=146)
Label(login_id, text="10th MARK's",font=('arial',15,"bold"),fg='red', bg='orange').place(x=550,y=200)
entry_9 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_9.place(x=700,y=200)
Label(login_id, text="12th MARK's",font=('arial',15,"bold"),fg='red',bg='orange').place(x=550,y=250)
entry_10 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_10.place(x=700,y=250)
Label(login_id, text="NATIONALITY",font=('arial',15,"bold"),fg='red', bg='orange').place(x=550,y=300)
entry_11 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_11.place(x=700,y=300)
Label(login_id, text="PHONE NO.",font=('arial',15,"bold"),fg='red', bg='orange').place(x=550,y=350)
entry_12 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_12.place(x=700,y=350)
Label(login_id, text="ADDRESS",font=('arial',15,"bold"),fg='red', bg='orange').place(x=550,y=400)
entry_13 = Entry(login_id, font=('arial',15),bg='orange',fg='red')
entry_13.place(x=700,y=400)

###########################################################################################################################

def printMsg():
    if((entry_1.get()=='Kaushal' and entry_2.get()=='844') or (entry_1.get()=='Ks' and entry_2.get()=='744') or (entry_1.get()=='Tiger' and entry_2.get()=='944') ):
        tkinter.messagebox.showinfo('login result', 'CONGRATULATIONS!! LOGIN SUCCESSFUL')
        createWindow()
    else:
        tkinter.messagebox.showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

button_1 = Button(login_id, text="LOGIN ",font=('arial',20,'bold'),bg='orange',fg='red', command=printMsg)
button_1.place(x=400,y=550)
button_2 = Button(login_id, text=" QUIT ",font=('arial',20,'bold'),bg='orange',fg='red', command=login_id.destroy)
button_2.place(x=550,y=550)

changeOnHover(button_1, "white", "orange")
changeOnHover(button_2, "white", "orange")


login_id.mainloop()
