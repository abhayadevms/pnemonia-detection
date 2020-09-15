# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pne.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
# created by :abhayadev   Email: mail.abhayadev@gmail.com
# keras 2.3.1 ,tensorflow 2.0
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5 import uic, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
import PyQt5.QtGui
import threading
import events
from events import Events
from threading import Event
import sys
import time
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
import shutil
import tempfile
import sys
from time import sleep
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import glob
import os
from PIL import Image
import cv2
from PIL import Image

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np




class Ui_MainWindow(QWidget):


    def clearall(self):
        self.label_2_NORMAL.hide()
        self.label_3_PHENOMIA.hide()
        self.lineEdit.clear()
        self.label_4_percntage.clear()

    def open(self):
        fileName = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEdit.setText(str(fileName))
        print(fileName)
        self.label_3_error.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 378)
        MainWindow.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 64, 611, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 351, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 60, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2_NORMAL = QtWidgets.QLabel(self.centralwidget)
        self.label_2_NORMAL.setGeometry(QtCore.QRect(20, 150, 181, 31))
        self.label_2_NORMAL.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2_NORMAL.setObjectName("label_2_NORMAL")
        self.label_3_PHENOMIA = QtWidgets.QLabel(self.centralwidget)
        self.label_3_PHENOMIA.setGeometry(QtCore.QRect(20, 150, 181, 31))
        self.label_3_PHENOMIA.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3_PHENOMIA.setObjectName("label_3_PHENOMIA")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 240, 181, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7_cantdetect = QtWidgets.QLabel(self.centralwidget)
        self.label_7_cantdetect.setGeometry(QtCore.QRect(20, 200, 181, 31))
        self.label_7_cantdetect.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_7_cantdetect.setObjectName("label_7_cantdetect")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(620, 64, 26, 21))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 100, 221, 181))
        self.label_2.setStyleSheet("background-color: rgb(253, 248, 248);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3_error = QtWidgets.QLabel(self.centralwidget)
        self.label_3_error.setGeometry(QtCore.QRect(10, 90, 251, 17))
        self.label_3_error.setObjectName("label_3_error")
        self.label_4_percntage = QtWidgets.QLabel(self.centralwidget)
        self.label_4_percntage.setGeometry(QtCore.QRect(220, 150, 181, 31))
        self.label_4_percntage.setStyleSheet("background-color: rgb(251, 247, 247);")
        #self.label_4_percntage.setText("")
        self.label_4_percntage.setObjectName("label_4_percntage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pneumonia detection"))
        self.label.setText(_translate("MainWindow", "enter the path of image floder"))
        self.pushButton.setText(_translate("MainWindow", "ok"))

        self.pushButton.clicked.connect(self.thread_event)
        self.label_2_NORMAL.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4e9a06;\">Norrmal </span></p></body></html>"))

        self.label_2_NORMAL.hide()

        self.label_3_PHENOMIA.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ef2929;\">PNEUMONIA</span></p></body></html>"))

        self.label_3_PHENOMIA.hide()

        self.pushButton_3.setText(_translate("MainWindow", "clear all"))
        self.pushButton_3.clicked.connect(self.clearall)
        self.label_7_cantdetect.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#eeeeec;\">can\'t detect </span></p></body></html>"))

        self.label_7_cantdetect.hide()
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton.clicked.connect(self.open)
        self.label_3_error.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ef2929;\">error: please enter the path </span></p></body></html>"))
        self.label_3_error.hide()



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


    def main_(self, stop_Event):
        line =self.lineEdit.text()
        if (len(line)!=0):
            self.label_3_error.hide()

            l=line[0]
            print(l)
            im = Image.open(l)
            img = im.resize((240, 240), Image.ANTIALIAS)
            img.save("output.jpeg")
            l_path ="output.jpeg"
            pixmap = QPixmap(l_path)
            self.label_2.setPixmap(pixmap)
            self.label_2.resize(pixmap.width(), pixmap.height())

            IMAGE_SIDE = 450
            current_dir = os.getcwd()

            MODEL_PATH = "/home/dev/Desktop/project/phenomia_toch/import_student/pneumonia_classifier_87model.h5"
            # dimensions of our images
            img_width, img_height = 450, 450
            # load the model we saved
            model = tf.keras.models.load_model(MODEL_PATH)
            model.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])
            # predicting images
            img = image.load_img(l,
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

            else:
                print("PNEUMONIA")




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