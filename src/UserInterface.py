# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import cv2
from backend.backend_code import *

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(684, 301)
        self.input_URL = QtWidgets.QLineEdit(Widget)
        self.input_URL.setGeometry(QtCore.QRect(110, 10, 291, 22))
        self.input_URL.setObjectName("input_URL")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 58, 15))
        self.label.setObjectName("label")
        self.input_masterPassword = QtWidgets.QLineEdit(Widget)
        self.input_masterPassword.setGeometry(QtCore.QRect(110, 110, 281, 22))
        self.input_masterPassword.setObjectName("input_masterPassword")

        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_generatedPassword = QtWidgets.QLabel(Widget)
        self.label_generatedPassword.setGeometry(QtCore.QRect(130, 80, 261, 16))
        self.label_generatedPassword.setObjectName("label_generatedPassword")

        self.lable_Username = QtWidgets.QLabel(Widget)
        self.lable_Username.setGeometry(QtCore.QRect(20, 50, 58, 15))
        self.lable_Username.setObjectName("lable_Username")
        self.input_username = QtWidgets.QLineEdit(Widget)

        self.input_username.setGeometry(QtCore.QRect(110, 50, 281, 22))
        self.input_username.setObjectName("input_username")
        self.label_Include = QtWidgets.QLabel(Widget)
        self.label_Include.setGeometry(QtCore.QRect(40, 150, 58, 15))
        self.label_Include.setObjectName("label_Include")
        self.chkbx_Lowecase = QtWidgets.QCheckBox(Widget)
        self.chkbx_Lowecase.setGeometry(QtCore.QRect(40, 180, 83, 21))
        self.chkbx_Lowecase.setChecked(True)
        self.chkbx_Lowecase.setObjectName("chkbx_Lowecase")
        self.chkbx_upercase = QtWidgets.QCheckBox(Widget)
        self.chkbx_upercase.setGeometry(QtCore.QRect(40, 210, 83, 21))
        self.chkbx_upercase.setChecked(True)
        self.chkbx_upercase.setObjectName("chkbx_upercase")
        self.chkbx_nubers = QtWidgets.QCheckBox(Widget)
        self.chkbx_nubers.setGeometry(QtCore.QRect(40, 240, 83, 21))
        self.chkbx_nubers.setChecked(True)
        self.chkbx_nubers.setObjectName("chkbx_nubers")
        self.chkbx_specialChars = QtWidgets.QCheckBox(Widget)
        self.chkbx_specialChars.setGeometry(QtCore.QRect(40, 270, 141, 21))
        self.chkbx_specialChars.setChecked(True)
        self.chkbx_specialChars.setObjectName("chkbx_specialChars")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(190, 150, 81, 16))
        self.label_3.setObjectName("label_3")

        self.input_Compexity = QtWidgets.QLineEdit(Widget)
        self.input_Compexity.setGeometry(QtCore.QRect(270, 150, 41, 22))
        self.input_Compexity.setObjectName("input_Compexity")

        self.btn_generatePassword = QtWidgets.QPushButton(Widget)
        self.btn_generatePassword.setGeometry(QtCore.QRect(220, 200, 121, 71))
        self.btn_generatePassword.setObjectName("btn_generatePassword")
        self.btn_generatePassword.clicked.connect(self.genPassword)


        self.btn_generateQR = QtWidgets.QPushButton(Widget)
        self.btn_generateQR.setGeometry(QtCore.QRect(460, 200, 121, 23))
        self.btn_generateQR.setObjectName("btn_generateQR")
        self.btn_generateQR.clicked.connect(self.genQRCode)
        self.list_paswords = QtWidgets.QListView(Widget)
        self.list_paswords.setGeometry(QtCore.QRect(410, 0, 256, 192))
        self.list_paswords.setObjectName("list_paswords")
        self.btn_TransferPasswords = QtWidgets.QPushButton(Widget)
        self.btn_TransferPasswords.setGeometry(QtCore.QRect(460, 230, 121, 23))
        self.btn_TransferPasswords.setObjectName("btn_TransferPasswords")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def genPassword(self, Widget):
        #ADD THE CODE GENERATIO CODE
        pw = Password(self.input_URL.text(), int(self.input_Compexity.text()),self.chkbx_nubers.isChecked(),self.chkbx_Lowecase.isChecked(),self.chkbx_upercase.isChecked(),self.chkbx_specialChars.isChecked())
        us = User(self.input_username.text(), self.input_masterPassword.text())
        print("btn clicked")
        self.label_generatedPassword.setText(pw.get_plaintext_password())
    def genQRCode(self, Widget):
        img = cv2.imread("/tmp/qr.png", cv2.IMREAD_ANYCOLOR)
        
        cv2.imshow("QR", img)
        cv2.waitKey(0)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "   URL:"))
        self.label_2.setText(_translate("Widget", "Master Password"))
        self.label_generatedPassword.setText(_translate("Widget", "RANDOMELY GENERATED PASSWORD"))
        self.lable_Username.setText(_translate("Widget", "Username"))
        self.label_Include.setText(_translate("Widget", "Include"))
        self.chkbx_Lowecase.setText(_translate("Widget", "lowercase"))
        self.chkbx_upercase.setText(_translate("Widget", "upercase"))
        self.chkbx_nubers.setText(_translate("Widget", "numbers"))
        self.chkbx_specialChars.setText(_translate("Widget", "specialCharacters"))
        self.label_3.setText(_translate("Widget", "Complexity"))
        self.input_Compexity.setText(_translate("Widget", "32"))
        self.btn_generatePassword.setText(_translate("Widget", "Generate "))
        self.btn_generateQR.setText(_translate("Widget", "Generate QR"))
        self.btn_TransferPasswords.setText(_translate("Widget", "Run Server"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
