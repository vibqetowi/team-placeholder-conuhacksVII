# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import cv2
from src.backend.backend_code import *
from src.to_json import *
from src.server.qr_code import *
from src.server.httpserver import *
from src.qr_code_auth import *
import pandas as pd
import json
import threading
import socket
from src.json_crypt import *



class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(700, 333)

        self.input_URL = QtWidgets.QLineEdit(Widget)
        self.input_URL.setGeometry(QtCore.QRect(110, 10, 291, 22))
        self.input_URL.setObjectName("input_URL")
        self.input_URL.setPlaceholderText("website name/url - mandatory field")

        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 58, 15))
        self.label.setObjectName("label")

        self.input_masterPassword = QtWidgets.QLineEdit(Widget)
        self.input_masterPassword.setGeometry(QtCore.QRect(110, 110, 281, 22))
        self.input_masterPassword.setObjectName("input_masterPassword")
        self.input_masterPassword.setPlaceholderText(
            "mandatory - we recommend pass phrases")

        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 121, 16))
        self.label_2.setObjectName("label_2")

        self.label_generatedPassword = QtWidgets.QLabel(Widget)
        self.label_generatedPassword.setGeometry(
            QtCore.QRect(130, 80, 261, 16))
        self.label_generatedPassword.setObjectName("label_generatedPassword")
        # this makes the password label selectable and copiable with the mouse
        self.label_generatedPassword.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        self.lable_Username = QtWidgets.QLabel(Widget)
        self.lable_Username.setGeometry(QtCore.QRect(20, 50, 58, 15))
        self.lable_Username.setObjectName("lable_Username")

        self.input_username = QtWidgets.QLineEdit(Widget)
        self.input_username.setGeometry(QtCore.QRect(110, 50, 281, 22))
        self.input_username.setObjectName("input_username")
        self.input_username.setPlaceholderText(
            "leave blank to generate a default value")

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

        self.input_Length = QtWidgets.QLineEdit(Widget)
        self.input_Length.setGeometry(QtCore.QRect(270, 150, 41, 22))
        self.input_Length.setObjectName("input_Length")

        self.btn_generatePassword = QtWidgets.QPushButton(Widget)
        self.btn_generatePassword.setGeometry(QtCore.QRect(220, 200, 200, 100))
        self.btn_generatePassword.setObjectName("btn_generatePassword")
        self.btn_generatePassword.clicked.connect(self.genPassword)

        # self.btn_generateQR = QtWidgets.QPushButton(Widget)
        # self.btn_generateQR.setGeometry(QtCore.QRect(460, 200, 150, 23))
        # self.btn_generateQR.setObjectName("btn_generateQR")
        # self.btn_generateQR.clicked.connect(self.genQRCode)

        self.list_paswords = QtWidgets.QListView(Widget)
        self.list_paswords.setGeometry(QtCore.QRect(410, 0, 256, 192))
        self.list_paswords.setObjectName("list_paswords")
        model = QtGui.QStandardItemModel()
        self.list_paswords.setModel(model)

        self.btn_TransferPasswords = QtWidgets.QPushButton(Widget)
        self.btn_TransferPasswords.setGeometry(QtCore.QRect(460, 230, 121, 44))
        self.btn_TransferPasswords.setObjectName("btn_TransferPasswords")
        self.btn_TransferPasswords.clicked.connect(self.exportPasswords)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def genPassword(self, Widget):

        self.input_username.setText('')
        url = self.input_URL.text()
        master_password = self.input_masterPassword.text()
        print(compute_bit_entropy(master_password))

        wb = Website(url,
                     int(self.input_Length.text()),
                     self.chkbx_nubers.isChecked(),
                     self.chkbx_Lowecase.isChecked(),
                     self.chkbx_upercase.isChecked(),
                     self.chkbx_specialChars.isChecked())

        # exception handling/ shaming the user when they make mistakes
        # I haven't slept ok, let me have some fun. Minh
        if not url:
            self.btn_generatePassword.setText(
                'URL IS MANDATORY DAMNIT\nLearn To Read!!!\nTry Again >:(')
            return
        elif compute_bit_entropy(master_password) < 40:
            self.btn_generatePassword.setText(
                'Your Master Password is Trash\nDude. Wikihow -> Passphrases\nTry Again >:(')
            return
        # if user unchecked all boxes
        elif wb.get_plaintext_password() == "Invalid Selection!":
            self.btn_generatePassword.setText(
                'Check At Least One Box\nShame On You!!!\nTry Again >:(')
            return

        # ADD THE CODE GENERATIO CODE
        us = User(master_password)
        entropy = wb.get_entropy()

        # update website username, if user did not put username
        # generate one
        if not self.input_username.text():
            self.input_username.setText(generate_username(url))
        wb.set_username(self.input_username.text())

        self.label_generatedPassword.setText(wb.get_plaintext_password())

        jv = JSONVault('vault.json')
        jv.write_data(self.input_username.text(), url,
                      wb.get_plaintext_password(), entropy)
        print("website saved")

        self.provide_password_report(entropy)
        self.addJsonToList()
        encrypt(master_password)

    def addJsonToList(self):
        model = QtGui.QStandardItemModel()
        self.list_paswords.setModel(model)
        values = []
        with open('vault.json') as json_f:
            data = json.load(json_f)
        for i in data:
            string = i['url'] + ':' + i['username'] + ':' + i['password']
            values.append(string)
            #print(string) 
        for j in values:
            item = QtGui.QStandardItem(j)
            model.appendRow(item)
        #self.gridLayout.addWidget(self.list_paswords, 1, 0, 1, 2)
        

    # changes the text on generate password btn to educate
    # the user on the strength of the password

    def provide_password_report(self, entropy):

        password_strength = ''
        if entropy < 30: 
            password_strength = 'unacceptable'
        elif entropy < 50:
            password_strength = 'weak'
        elif entropy < 100:
            password_strength = 'medium'
        else:
            password_strength = 'strong'

        self.btn_generatePassword.setText(
            f'Password entropy: {int(entropy)} bits \nThis Password is {password_strength} \nClick to generate another')

    # def genQRCode(self, Widget):
    #     file_path = 'qr.png'
    #     file_reader = JSONFileReader('vault.json')
    #     json_str = file_reader.read_file()
    #     qr_code = QR_Code(json_str)
    #     qr_code.generate_qr_code(file_path)
    #     print(json_str)

    #     img = cv2.imread("qr.png", cv2.IMREAD_ANYCOLOR)

    #     cv2.imshow("QR", img)
    #     cv2.waitKey(0)
    def exportPasswords(self):
        url = "http://"+str(self.getNetworkIp())+":80/download"
        generate_qr(url)
        img = cv2.imread("qr_code.png", cv2.IMREAD_ANYCOLOR)

        cv2.imshow("QR", img)
        cv2.waitKey(0)
        print("img displayed")
        cv2.destroyAllWindows()

        httpd = HTTPServer(('',80),MyHandler)
        stop_server = threading.Timer(60.0,httpd.shutdown)
        stop_server.start()

        httpd.serve_forever()
        

    def getNetworkIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(('<broadcast>', 0))
        return s.getsockname()[0]

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "   URL:"))
        self.label_2.setText(_translate("Widget", "Master Password"))
        self.label_generatedPassword.setText(
            _translate("Widget", "PASSWORD WILL BE GENERATED HERE"))
        self.lable_Username.setText(_translate("Widget", "Username"))
        self.label_Include.setText(_translate("Widget", "Include"))
        self.chkbx_Lowecase.setText(_translate("Widget", "lowercase"))
        self.chkbx_upercase.setText(_translate("Widget", "upercase"))
        self.chkbx_nubers.setText(_translate("Widget", "numbers"))
        self.chkbx_specialChars.setText(
            _translate("Widget", "specialCharacters"))
        self.label_3.setText(_translate("Widget", "Length"))
        self.input_Length.setText(_translate("Widget", "32"))
        self.btn_generatePassword.setText(
            _translate("Widget", "Generate Password"))

        # self.btn_generateQR.setText(_translate("Widget", "Generate QR"))
        self.btn_TransferPasswords.setText(
            _translate("Widget", "Export Vault"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
