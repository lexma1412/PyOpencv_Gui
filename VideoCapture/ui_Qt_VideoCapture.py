# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\VideoCapture\Qt_VideoCapture.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoCapture_Gui(object):
    def setupUi(self, VideoCapture_Gui):
        VideoCapture_Gui.setObjectName("VideoCapture_Gui")
        VideoCapture_Gui.resize(916, 620)
        self.Start_pushButton = QtWidgets.QPushButton(VideoCapture_Gui)
        self.Start_pushButton.setGeometry(QtCore.QRect(50, 10, 100, 100))
        self.Start_pushButton.setStyleSheet("border-color: rgb(66, 69, 183);\n"
"background-color: green;\n"
"border-width: 3px;        \n"
"border-style: solid;\n"
"border-radius: 50px;")
        self.Start_pushButton.setObjectName("Start_pushButton")
        self.Stop_pushButton = QtWidgets.QPushButton(VideoCapture_Gui)
        self.Stop_pushButton.setGeometry(QtCore.QRect(190, 10, 100, 100))
        self.Stop_pushButton.setStyleSheet("border-color: rgb(66, 69, 183);\n"
"background-color: red;\n"
"border-width: 3px;        \n"
"border-style: solid;\n"
"border-radius: 50px;")
        self.Stop_pushButton.setObjectName("Stop_pushButton")
        self.Video_label = QtWidgets.QLabel(VideoCapture_Gui)
        self.Video_label.setGeometry(QtCore.QRect(30, 130, 854, 480))
        self.Video_label.setText("")
        self.Video_label.setObjectName("Video_label")
        self.FPS_label = QtWidgets.QLabel(VideoCapture_Gui)
        self.FPS_label.setGeometry(QtCore.QRect(40, 150, 101, 21))
        self.FPS_label.setObjectName("FPS_label")

        self.retranslateUi(VideoCapture_Gui)
        QtCore.QMetaObject.connectSlotsByName(VideoCapture_Gui)

    def retranslateUi(self, VideoCapture_Gui):
        _translate = QtCore.QCoreApplication.translate
        VideoCapture_Gui.setWindowTitle(_translate("VideoCapture_Gui", "Form"))
        self.Start_pushButton.setText(_translate("VideoCapture_Gui", "Start"))
        self.Stop_pushButton.setText(_translate("VideoCapture_Gui", "Stop"))
        self.FPS_label.setText(_translate("VideoCapture_Gui", "<html><head/><body><p><span style=\" font-weight:600; color:#f80000;\">None</span></p></body></html>"))
