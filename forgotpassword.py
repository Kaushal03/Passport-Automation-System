from tkinter import *
from tkinter import messagebox
from hoverfunc import changeOnHover

root = Tk()
root.title("FORGOT PASSWORD")
root.geometry("630x400")

label0 = Label(root, text="New Password", font=("arial 20 bold underline"), relief=FLAT)
label0.place(x=220, y=30)

label1 = Label(root, text="Enter Your's New Password : ", font=("ariel 15 bold"), relief=FLAT)
label1.place(x=20,y=90)

label2 = Label(root, text="Confirm Your's Password    : ", font=("ariel 15 bold"), relief=FLAT)
label2.place(x=20,y=150)


entry1 = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
entry1.place(x=320,y=90)

entry2 = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
entry2.place(x=320,y=150)


send_button = Button(root, text=" SUBMIT ", font=("ariel 15 bold"),bd=3)
send_button.place(x=170,y=270)

verify_button = Button(root, text="CANCEL", font=("ariel 15 bold"),bd=3)
verify_button.place(x=300, y=270)


changeOnHover(send_button, "cyan", "white")
changeOnHover(verify_button, "cyan", "white")

root.mainloop()
