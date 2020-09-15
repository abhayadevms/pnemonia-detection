# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PATH1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from keras.preprocessing import image

import tensorflow as tf
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
import threading
from PIL import Image, ImageOps
import os

class Ui_MainWindow(QWidget):
    def open(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File')
        self.lineEdit.setText(str(fileName[0]))
        print(fileName[0])
        self.label_2_ERROR.hide()
    def clear_(self):
        self.lineEdit.clear()
        self.label_PIC_DIS.clear()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1072, 567)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.312591, x2:0, y2:1, stop:0 rgba(15, 116, 204, 255), stop:0.420792 rgba(40, 170, 202, 255), stop:1 rgba(40, 170, 202, 255));")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 741, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(9, 163, 252);\n"
"font: 25 11pt \"Umpush\";\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_PROCEED = QtWidgets.QPushButton(Form)
        self.pushButton_PROCEED.setGeometry(QtCore.QRect(660, 160, 261, 51))
        self.pushButton_PROCEED.setStyleSheet("alternate-background-color: rgb(9, 163, 252);\n"
"\n"
"font: 21pt \"Sawasdee\";\n"
"color: rgb(238, 238, 236);\n"
" \n"
" alternate-background-color: rgb(9, 163, 252);\n"
"\n"
" border-color: blue;\n"
" border-width:1px;\n"
"\n"
"background-color: rgb(40, 170, 202, 255);\n"
"\n"
" ")
        self.pushButton_PROCEED.setObjectName("pushButton_PROCEED")

        #######################

        self.pushButton_PROCEED.clicked.connect(self.thread_event)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(880, 100, 41, 41))
        self.toolButton.setStyleSheet("alternate-background-color: rgb(9, 163, 252);\n"
"\n"
"font: 21pt \"Sawasdee\";\n"
"\n"
" \n"
" alternate-background-color: rgb(9, 163, 252);\n"
"\n"
" border-color: red;\n"
" border-width:1px;\n"
"\n"
"background-color: rgb(40, 170, 202, 255);\n"
"\n"
" ")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.open)
        self.label_PATH = QtWidgets.QLabel(Form)
        self.label_PATH.setGeometry(QtCore.QRect(140, 70, 401, 31))
        self.label_PATH.setStyleSheet("background-color: rgb(15, 116, 204, 255);\n"
"font: 25 11pt \"Umpush\";")
        self.label_PATH.setObjectName("label_PATH")
        self.label_2_ERROR = QtWidgets.QLabel(Form)
        self.label_2_ERROR.setGeometry(QtCore.QRect(140, 140, 281, 31))
        self.label_2_ERROR.setStyleSheet("background-color: rgb(15, 116, 204, 255);\n"
"font: 25 11pt \"Umpush\";")
        self.label_2_ERROR.setObjectName("label_2_ERROR")
        self.label_2_ERROR.hide()
        self.label_HEALTH = QtWidgets.QLabel(Form)
        self.label_HEALTH.setGeometry(QtCore.QRect(140, 290, 281, 71))
        self.label_HEALTH.setStyleSheet("font: 75 11pt \"Sawasdee\";\n"
"background-color: rgb(40, 170, 202, 255);")
        self.label_HEALTH.setObjectName("label_HEALTH")
        self.label_HEALTH.hide()


        self.label_PIC_DIS = QtWidgets.QLabel(Form)
        self.label_PIC_DIS.setGeometry(QtCore.QRect(570, 240, 361, 321))
        self.label_PIC_DIS.setText("")
        self.label_PIC_DIS.setObjectName("label_PIC_DIS")
        self.label_PNEU = QtWidgets.QLabel(Form)
        self.label_PNEU.setGeometry(QtCore.QRect(140, 290, 281, 71))
        self.label_PNEU.setStyleSheet("font: 75 11pt \"Sawasdee\";\n"
"background-color: rgb(40, 170, 202, 255);")
        self.label_PNEU.setObjectName("label_PNEU")
        self.label_PNEU.hide()





        self.pushButton_2_BACK = QtWidgets.QPushButton(Form)
        self.pushButton_2_BACK.setGeometry(QtCore.QRect(140, 490, 261, 51))
        self.pushButton_2_BACK.setStyleSheet("background-color: rgb(40, 170, 202, 255);\n"
"color: rgb(238, 238, 236);\n"
"font: 75 20pt \"Sawasdee\";\n"
"\n"
"\n"
"\n"
"\n"
" border-color: blue;\n"
" ")
        self.pushButton_2_BACK.setObjectName("pushButton_2_BACK")
        self.pushButton_2_BACK.clicked.connect(self.clear_)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PNEUMONIA DETECTION"))
        self.pushButton_PROCEED.setText(_translate("Form", "Proceed"))
        self.toolButton.setText(_translate("Form", "📂"))
        self.label_PATH.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:15pt; color:#eeeeec;\">Enter the Path</span></p></body></html>"))
        self.label_2_ERROR.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; color:#cc0000;\">Error: Please enter the path</span></p></body></html>"))
        self.label_HEALTH.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#eeeeec;\">HEALTHY</span></p></body></html>"))
        self.label_PNEU.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#eeeeec;\">PNEUMONIA</span></p></body></html>"))
        self.pushButton_2_BACK.setText(_translate("Form", "◀  CLEAR"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


    def main_(self, stop_Event):
        line =self.lineEdit.text()
        if (len(line)!=0):
            self.label_2_ERROR.hide()
            l=line[0]
            print(line)
            im = Image.open(line)
            img = im.resize((450, 350), Image.ANTIALIAS)
            img.save("output.jpeg")
            l_path ="output.jpeg"
            pixmap = QPixmap(l_path)
            self.label_PIC_DIS.setPixmap(pixmap)
            self.label_PIC_DIS.resize(pixmap.width(), pixmap.height())

            IMAGE_SIDE = 450
            current_dir = os.getcwd()

            MODEL_PATH = "/home/dev/Desktop/project/phenomia_toch/import_student/pneumonia_classifier_87model.h5"

            # dimensions of our images
            img_width, img_height = 450, 450
            # load the model we saved
            model = tf.keras.models.load_model(MODEL_PATH)
            model.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])
            # predicting images
            img = image.load_img(line,
                                 target_size=(img_width, img_height))
            img1 = img.convert('L')  # convert a gray scale
            y = np.expand_dims(img1, axis=-1)
            x = image.img_to_array(y)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            prediction = model.predict(images)
            print(prediction)

            print("Prediction is:  {}".format(prediction))
            pred_list = prediction[0].tolist()
            max_index = pred_list.index(max(pred_list))
            if max_index == 0:
                print("NORMAL")
                self.label_PNEU.hide()
                self.label_HEALTH.show()

            else:
                print("PNEUMONIA")
                self.label_PNEU.show()
                self.label_HEALTH.hide()
        else:
            self.label_2_ERROR.show()

    def thread_event(self,stop_event):
        self.stop_event = threading.Event()
        self.c_thread = threading.Thread(target=self.main_, args=(self.stop_event,))
        self.c_thread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    M= MainWindow()
    M.show()
    sys.exit(app.exec_())

