import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from Contour.ui_Qt_Contour import Ui_Contour_Gui
from Contour.Contour_Alg import FindContour

DictContourMode = {
    "RETR_EXTERNAL": 0,
    "RETR_LIST": 1,
    "RETR_CCOMP": 2,
    "RETR_TREE": 3,
    "RETR_FLOODFILL": 4
}

DictContourMethod = {
    "CHAIN_APPROX_NONE": 0,
    "CHAIN_APPROX_SIMPLE": 1,
    "CHAIN_APPROX_TC89_L1": 2,
    "CHAIN_APPROX_TC89_KCOS": 3
}

class MyContour_Gui(QtWidgets.QWidget, Ui_Contour_Gui):
    def __init__(self):
        super(MyContour_Gui, self).__init__()
        self.setupUi(self)
        # Connect
        self.ContourAlg = FindContour(".\\Contour\\test_img.png") 
        self.FindContour_pushButton.clicked.connect(self.RunAlg)
        self.ContourMethod_comboBox.currentTextChanged.connect(self.MethodChanged)
        self.ContourMode_comboBox.currentTextChanged.connect(self.ModeChanged)

    @pyqtSlot()
    def RunAlg(self):
        self.ContourAlg.FindContourAlg()

    @pyqtSlot()
    def MethodChanged(self):
        self.ContourAlg.ContourMethod = DictContourMethod[self.ContourMethod_comboBox.currentText()]

    @pyqtSlot()
    def ModeChanged(self):
        self.ContourAlg.ContourMode = DictContourMode[self.ContourMode_comboBox.currentText()]
        
