import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from ImageFilter.ui_Qt_ImageFilter import Ui_ImageFilter_Gui
from ImageFilter.ImageFilter_Alg import *


class MyImageFilter_Gui(QtWidgets.QWidget, Ui_ImageFilter_Gui):
    def __init__(self):
        super(MyImageFilter_Gui, self).__init__()
        self.setupUi(self)

        # Init algorithm object
        self.Alg = ImageFilter(".\\ImageFilter\\test_img.png",None)
        # Connect
        self.GaussisanFilter_pushButton.clicked.connect(self.GaussianFilterRun)
        self.MedianFilter_pushButton.clicked.connect(self.MedianFilterRun)
        self.LaplacianFilter_pushButton.clicked.connect(self.LaplacianFilterRun)
    

    @pyqtSlot()
    def GaussianFilterRun(self):
        self.Alg.RunGaussianFilterAlg(int(self.Kernelsize_comboBox.currentText()), int(self.SigmaX_comboBox.currentText()))
    
    @pyqtSlot()
    def MedianFilterRun(self):
        self.Alg.RunMedianFilterAlg(int(self.MedianKernelsize_comboBox.currentText()))

    @pyqtSlot()
    def LaplacianFilterRun(self):
        self.Alg.RunLaplacianFilterAlg()
