import random
import smtplib
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QRadioButton, QFileDialog
from PyQt5.uic import loadUi
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='india123abcd$',
                              host='127.0.0.1',
                              database='passport')
cursor = conn.cursor()


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
        cursor.execute("SELECT username,password from user where username like '"+username + "'and password like '"+password+"'")
        result = cursor.fetchone()
        if result == None:
            QMessageBox.critical(self,"","wrong username or password,Please try again !!")
            print("username not in database or username and password does not match")
            print("Please sign up first")
        else:
            QMessageBox.information(self," ","Successfully logged-in ")
            print(self," ","Successfully logged in as: ",username,"and password: ",password)
            self.loginbutton.pressed.connect(self.gotocreate_register)            
    

    def gotocreate(self):
        
        signup=Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_otp(self):
        forgotpwdbutton=Otp()
        widget.addWidget(forgotpwdbutton)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_register(self):
         register=Register()
         widget.addWidget(register)
         widget.setCurrentIndex(widget.currentIndex()+1)


class Signup(QDialog):
    def __init__(self):
        super(Signup,self).__init__()
        loadUi("signup.ui",self)
        self.signupbutton.clicked.connect(self.signupfunction)
        self.login.clicked.connect(self.gotocreate_login)

 
    def  signupfunction(self):
    	
        email=self.email.text()
        mobileno=self.mobileno.text()
        username_3=self.username_3.text()
        password=self.password.text()
        confirmpass=self.confirmpass.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            sql = """INSERT INTO user(email, mobileno, username, password, confirm_password)VALUES (%s, %s, %s, %s, %s)"""
            data=(email,mobileno,username_3,password,confirmpass)
            try:
                cursor.execute(sql,data)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close()

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
        self.cancelotp.clicked.connect(self.gotocreate_login)
        
  
   
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
         QMessageBox.information(self,"OTP","OTP sent successfully")
         print(self,"OTP","OTP sent successfully to ",emailid)
         s.quit()
     except:
         QMessageBox.critical(self,"OTP","Please enter vaild mail address or check the internet connection")

    def verifyfunction(self):
        otpno=self.otpno.text()
        if otp == otpno:
            QMessageBox.information(self,"OTP","Success")
            self.verifyotp.pressed.connect(self.gotocreate_forgotpwd)
            
        else:
            QMessageBox.critical(self,"OTP","Failed")
    
    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_forgotpwd(self):
         forgotpwd=Forgotpassword()
         widget.addWidget(forgotpwd)
         widget.setCurrentIndex(widget.currentIndex()+1)

class Forgotpassword(QDialog):
    def __init__(self):
        super(Forgotpassword,self).__init__()
        loadUi("forgotpassword.ui",self)
        self.cancelpwd.clicked.connect(self.gotocreate_login)

    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)


class Register(QDialog):
    def __init__(self):
        super(Register,self).__init__()
        loadUi("registration.ui",self)
        global filename,filename1,filename2,filename3,filename4
        self.register_2.clicked.connect(self.registerfunction)


    def registerfunction(self):
        fname=self.fname.text()
        lname=self.lname.text()
        username=self.username.text()
        dob=self.dob.text()
        gender=self.gender.text()
        mobileno=self.mobileno.text()
        email=self.email.text()
        nationality=self.nationality.text()
        martialstatus=self.martialstatus.text() 
        aadhar=self.aadhar.text()
        pan=self.pan.text()
        driving=self.driving.text()
        _10mark=self._10mark.text()
        _12mark=self._12mark.text()
        sql = """INSERT INTO user_register(fname,lname,username,dob,gender,mobileno,email,nationality,martialstatus,aadhar,pan,driving,_10mark,_12mark)VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s, %s, %s, %s)"""
        data=(fname,lname,username,dob,gender,mobileno,email,nationality,martialstatus,aadhar,pan,driving,_10mark,_12mark)
        try:
            cursor.execute(sql,data)
            conn.commit()
            QMessageBox.information(self," ","Registered successfully")
        except Exception as e:
            print(e)
            QMessageBox.critical(self," ","Registered Failed")
            conn.rollback()
            conn.close()

                
               # print(self," ","Successfully created account with email: ",email,"and password: ", password)
        

    


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(900)
widget.setFixedWidth(1200)
widget.show()
app.exec_() 
