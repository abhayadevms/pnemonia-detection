# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PATH2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PATH1 import MainWindow
from PyQt5.QtWidgets import QFileDialog, QWidget

class Ui_Form(QWidget):
    def open_main(self):
        Form.hide()
        dialog = QtWidgets.QDialog()
        dialog.ui = MainWindow()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1072, 566)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.312591, x2:0, y2:1, stop:0 rgba(15, 116, 204, 255), stop:0.420792 rgba(40, 170, 202, 255), stop:1 rgba(40, 170, 202, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 100, 761, 91))
        self.label.setStyleSheet("background-color: rgb(15, 116, 204, 255);\n"
"font: 11pt \"Sawasdee\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 370, 771, 61))
        self.pushButton.setStyleSheet("font: italic 11pt \"Ubuntu\";\n"
"border-color: red;\n"
" border-width:1px;\n"
"\n"
"background-color: rgb(40, 170, 202, 255);\n"
"font: 57 italic 24pt \"Ubuntu\";\n"
"\n"
"\n"
"font: 20pt \"URW Gothic L\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PNEUMONIA DETECTION"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#eeeeec;\">PNEUMONIA DETECTION</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "CLICK FOR PNEUMONIA DETECTION"))
        self.pushButton.clicked.connect(self.open_main)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

