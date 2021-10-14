import random
import smtplib
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.signup.clicked.connect(self.gotocreate)
        self.forgotpwdbutton.clicked.connect(self.gotocreate_otp)
    
    def loginfunction(self):
        username= self.username.text()
        password= self.password.text()
        QMessageBox.information(self," ","Successfully logged-in ")
        print(self," ","Successfully logged in as: ",username,"and password: ",password)
    

    def gotocreate(self):
        signup=Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_otp(self):
        forgotpwdbutton=Otp()
        widget.addWidget(forgotpwdbutton)
        widget.setCurrentIndex(widget.currentIndex()+1)         




class Signup(QDialog):
    def __init__(self):
        super(Signup,self).__init__()
        loadUi("signup.ui",self)
        self.signupbutton.clicked.connect(self.signupfunction)
        self.login.clicked.connect(self.gotocreate_login)


    def signupfunction(self):
        email=self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            QMessageBox.information(self," ","Account created successfully")
            print(self," ","Successfully created account with email: ",email,"and password: ", password)
        else:
            QMessageBox.critical(self," ","Password does not match")

    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)


class Otp(QDialog):
    def __init__(self):
        super(Otp,self).__init__()
        loadUi("otp.ui",self)
        self.sendotp.clicked.connect(self.sendfunction)
        self.verifyotp.clicked.connect(self.verifyfunction)
    
    def sendfunction(self):
     global otp
     try:    
         emailid=self.emailid.text()
         s = smtplib.SMTP("smtp.gmail.com",587)
         s.starttls()
         s.login("projecti2001work@gmail.com" , "ProjectWork2001")
         otp = random.randint(1000,9999)
         otp = str(otp)
         s.sendmail("projecti2001work@gmail.com" ,emailid , otp)
         QMessageBox.about(self,"OTP","OTP sent successfully to ",emailid)
         s.quit()
     except:
         QMessageBox.critical(self,"OTP","Please enter vaild mail address or check the internet connection")


    def verifyfunction(self):
        otpno=self.otpno.text()
        if otp == otpno:
            QMessageBox.information(self,"OTP","Success")
        else:
            QMessageBox.critical(self,"OTP","Failed")


   



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_()