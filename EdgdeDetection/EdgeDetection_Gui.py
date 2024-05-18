import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from EdgdeDetection.ui_Qt_EdgeDetection import Ui_EdgeDetection_Gui
from EdgdeDetection.EdgeDetection_Alg import *


class MyEdgdeDetection_Gui(QtWidgets.QWidget, Ui_EdgeDetection_Gui):
    def __init__(self):
        super(MyEdgdeDetection_Gui, self).__init__()
        self.setupUi(self)

        # Init algorithm object
        self.Alg = EdgeDetection(".\\EdgdeDetection\\test_img.png","CannyEdge")
        # Connect
        self.hysteresislowth_horizontalSlider.valueChanged.connect(self.hysteresislowthUpdate)
        self.hysteresishighth_horizontalSlider.valueChanged.connect(self.hysteresishighthUpdate)
        self.Kernelsize_comboBox.currentTextChanged.connect(self.KernelsizeChanged)
        self.L2norm_checkBox.toggled.connect(self.L2normChanged)

    @pyqtSlot()
    def hysteresislowthUpdate(self):
        self.lowthreshold_textEdit.setText(str(self.hysteresislowth_horizontalSlider.value()))
        self.Alg.hysteresislowth = self.hysteresislowth_horizontalSlider.value()
        self.Alg.RunCannyEdgeAlg()
    
    def hysteresishighthUpdate(self):
        self.highthreshold_textEdit.setText(str(self.hysteresishighth_horizontalSlider.value()))
        self.Alg.hysteresishighth = self.hysteresishighth_horizontalSlider.value()
        self.Alg.RunCannyEdgeAlg()

    def KernelsizeChanged(self):
        self.Alg.Kernelsize = int(self.Kernelsize_comboBox.currentText())
        self.Alg.RunCannyEdgeAlg()

    def L2normChanged(self):
        self.Alg.L2Grad = self.L2norm_checkBox.isChecked()
        self.Alg.RunCannyEdgeAlg()