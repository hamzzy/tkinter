# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from os import system
import  subprocess

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def alert(self,title,message):
       self.msgbox=QtGui.QMessageBox()
       self.msgbox.setIcon(QtGui.QMessageBox.Warning)
       self.msgbox.setWindowTitle(title)
       self.msgbox.setText(message)
       self.msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
       self.msgbox.exec_()
    def start(self):
        self.name=self.lineEdit.text()
        self.passkey = self.lineEdit_2.text()
        self. passe = self.lineEdit_3.text()
        if self.passkey==self.passe and len(self.passkey)==7:
         cmd='netsh wlan set hostednetwork mode=allow ssid={} key={}'.format(self.name,self.passkey)
         cmd2='netsh wlan start hostednetwork'
         cmds=[cmd,cmd2]
         for c in cmds:
            subprocess.Popen(c,shell=True)
        elif self.name=='' and self.passkey=='':
            self.alert('warning', 'passname or passkey not correct')
        else:
            self.alert('warning','password must be  seven characters')


    def stop(self):
        c='netsh wlan stop hostednetwork'
        subprocess.Popen(c, shell=True)
    def resetpass(self):
        name=self.lineEdit_2.text()
        system('netsh wlan change key={} '.format(name))
        self.alert('pass change','it has been change')
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 480)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 80, 221, 26))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 221, 26))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 190, 221, 26))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 300, 96, 26))
        self.pushButton.clicked.connect(self.start)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 300, 96, 26))
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 300, 96, 26))
        self.pushButton_3.clicked.connect(self.resetpass)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 85, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "start", None))
        self.pushButton_2.setText(_translate("Form", "stop", None))
        self.pushButton_3.setText(_translate("Form", "reset ", None))
        self.label.setText(_translate("Form", "Hotspot name", None))
        self.label_2.setText(_translate("Form", "Password", None))
        self.label_3.setText(_translate("Form", "re-Password", None))

if __name__ == "__main__":
        import sys
        app = QtGui.QApplication(sys.argv)
        myapp = QtGui.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(myapp)
        myapp.show()
        sys.exit(app.exec_())


