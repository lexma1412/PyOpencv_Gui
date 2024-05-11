import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow_Gui import Ui_MainWindow
from BlobDetection.BlobDetection_Gui import MyBlobDetection_Gui

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        #self.BlobDetection_instance = BlobDetection_instance
        self.Called_BlobDetection.clicked.connect(self.on_click_Open)
        self.BlobDetection_ui = MyBlobDetection_Gui()

    @pyqtSlot()
    def on_click_Open(self):
        print('PyQt5 button click')
        self.BlobDetection_ui.show()