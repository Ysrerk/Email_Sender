import sys
from PyQt5.QtWidgets import *

from PyQt5.QtGui import *
import sqlite3
import smtplib

connect=sqlite3.connect("email.db")
cursor=connect.cursor()

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Send E-Mail Application @yasarerkan")
        self.setGeometry(150,150,650,600)
        self.setStyleSheet("background-color:#99e699;")
        self.ui()


    def ui(self):

        self.title=QLabel("E-MAIL SENDER APPLICATION",self)
        self.title.move(250,50)

        self.senderemail=QLineEdit(self)
        self.senderemail.move(100,100)
        self.senderemail.resize(500,25)
        self.senderemail.setStyleSheet("background-color:#ffffff;")
        self.senderemail.setPlaceholderText("Please write SENDER email adress@gmail.com")

        self.receiveremail = QLineEdit(self)
        self.receiveremail.move(100, 150)
        self.receiveremail.resize(500, 25)
        self.receiveremail.setStyleSheet("background-color:#e085c2;")
        self.receiveremail.setPlaceholderText("Please write RECEIVER mail adress ")

        self.password=QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(100,200)
        self.password.setStyleSheet("background-color:#ffffff;")
        self.password.setPlaceholderText("Enter Password")

        self.textm=QTextEdit(self)
        self.textm.move(100,250)
        self.textm.resize(500,250)
        self.textm.setStyleSheet("background-color:#ff751a;")

        self.sendbtn=QPushButton("Send",self)
        self.sendbtn.move(300,550)
        self.sendbtn.resize(100,25)
        self.sendbtn.setStyleSheet("background-color:#6666ff;")
        self.sendbtn.clicked.connect(self.send_email)



        self.show()
    def send_email(self):
        sender=self.senderemail.text()
        receiver=self.receiveremail.text()
        message=self.textm.toPlainText()
        password=self.password.text()
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo
        server.starttls()
        server.login(sender,password)
        server.sendmail(sender,receiver,message)


        server.close()


        cursor.execute("INSERT INTO emails VALUES (?,?,?,?)",(None,sender,receiver,message))
        connect.commit()
        QMessageBox.information(self,"Qmessagebox info","E mail sended and saved")
        self.senderemail.setText("")
        self.receiveremail.setText("")
        self.textm.setText("")
        self.password.setText("")



def main():
    application=QApplication(sys.argv)
    window=Window()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()

