from tkinter import *
from tkinter import messagebox
import smtplib
import random

from hoverfunc import changeOnHover

root = Tk()
root.title("Send OTP Via Email")
root.geometry("565x400")

email_label = Label(root, text="Enter Your's Email: ", font=("ariel 15 bold"), relief=FLAT)
email_label.grid(row=0, column=0, padx=15, pady=60)

email_entry = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
email_entry.grid(row=0, column=1, padx=12, pady=60)
email_entry.focus()

otp_label = Label(root, text="Enter Your's OTP: ", font=("ariel 15 bold"), relief=FLAT)
otp_label.grid(row=5, column=0, padx=25, pady=60)

otp_entry = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
otp_entry.grid(row=5, column=1, padx=12, pady=60)
otp_entry.focus()


def send():
    global otp
    try:
        s = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number 
        s.starttls()
        s.login("ksprojectcode@gmail.com" , "coco789@")
        otp = random.randint(1000, 9999)
        otp = str(otp)
        s.sendmail("sender_email" , email_entry.get() , otp)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")
        s.quit()
    
    except:
        messagebox.showinfo("Send OTP via Email", "Please enter the valid email address OR check an internet connection")

def verify():
    if otp == otp_entry.get():
        messagebox.showinfo("OTP INFORMATION", "SUCCESS ")
    else:
        messagebox.showinfo("OTP INFORMATION", "FAILED ")




send_button = Button(root, text=" SEND OTP ", font=("ariel 15 bold"),bd=3,command=send)
send_button.place(x=210,y=120)

verify_button = Button(root, text="VERIFY OTP", font=("ariel 15 bold"),bd=3,command=verify)
verify_button.place(x=210, y=270)


changeOnHover(send_button, "white", "cyan")
changeOnHover(verify_button, "white", "cyan")

root.mainloop()

