import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow_Gui import Ui_MainWindow
from BlobDetection.BlobDetection_Gui import MyBlobDetection_Gui
from EdgdeDetection.EdgeDetection_Gui import MyEdgdeDetection_Gui
from VideoCapture.VideoCapture_Gui import MyVideoCapture_Gui

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.Called_BlobDetection.clicked.connect(self.on_click_Called_BlobDetection)
        self.Called_EdgeDetection.clicked.connect(self.on_click_Called_EdgeDetection)
        self.Called_Video.clicked.connect(self.on_click_Called_VideoCapture)
        self.BlobDetection_Gui = None 
        self.EdgdeDetection_Gui = None
        self.VideoCapture_Gui = None

    @pyqtSlot()
    def on_click_Called_BlobDetection(self):
        print('PyQt5 button click')
        if (self.BlobDetection_Gui == None):
            self.BlobDetection_Gui= MyBlobDetection_Gui()
        self.BlobDetection_Gui.show()
    def on_click_Called_EdgeDetection(self):
        print('PyQt5 button click')
        if (self.EdgdeDetection_Gui == None):
            self.EdgdeDetection_Gui = MyEdgdeDetection_Gui()
        self.EdgdeDetection_Gui.show()
    def on_click_Called_VideoCapture(self):
        print('PyQt5 button click')
        if (self.VideoCapture_Gui == None):
            self.VideoCapture_Gui = MyVideoCapture_Gui()
        self.VideoCapture_Gui.show()

    # Overwrite method closeEvent from class QMainWindow.
    def closeEvent(self, event) -> None:
        if self.VideoCapture_Gui.Alg.isRunning():
            self.VideoCapture_Gui.Alg.quit()
         # Accept the event
        event.accept()
