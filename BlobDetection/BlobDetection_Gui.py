import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from BlobDetection.ui_Qt_BlobDetection import Ui_BlobDtection_Gui
from BlobDetection.BlobDetection_Alg import *

# define CONSTANT
NUM_PARAM = 10

class MyBlobDetection_Gui(QtWidgets.QWidget, Ui_BlobDtection_Gui):
    def __init__(self):
        super(MyBlobDetection_Gui, self).__init__()
        self.setupUi(self)
         # Init Algorithm object
        self.Alg_chosen = self.BlobDetection_comboBox.currentText()
        self.Alg = BlobDetection(".\\BlobDetection\\blob_test.png", self.Alg_chosen)
        #
        self.BlobDetection_comboBox.currentTextChanged.connect(self.AlgChanged)
        cv2.namedWindow( self.Alg.cvnameWindow)
        # Connect Sliderbar to TextEdit
        self.minThreshold_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.minThreshold_horizontalSlider.value(),self.minThreshold_textEdit,1))
        self.maxThreshold_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.maxThreshold_horizontalSlider.value(),self.maxThreshold_textEdit,1))
        self.minArea_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.minArea_horizontalSlider.value(),self.minArea_textEdit,1))
        self.maxArea_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.maxArea_horizontalSlider.value(),self.maxArea_textEdit,1))
        self.minCircularity_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.minCircularity_horizontalSlider.value(),self.minCircularity_textEdit,100))
        self.maxCircularity_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.maxCircularity_horizontalSlider.value(),self.maxCircularity_textEdit,100))
        self.minConvexity_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.minConvexity_horizontalSlider.value(),self.minConvexity_textEdit,100))
        self.maxConvexity_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.maxConvexity_horizontalSlider.value(),self.maxConvexity_textEdit,100))
        self.minInertiaRatio_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.minInertiaRatio_horizontalSlider.value(),self.minInertiaRatio_textEdit,100))
        self.maxInertiaRatio_horizontalSlider.valueChanged.connect(lambda: self.TexteditUpdated(self.maxInertiaRatio_horizontalSlider.value(),self.maxInertiaRatio_textEdit,100))
        # Connect Sliderbar to Param
        self.minThreshold_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated(1))
        self.maxThreshold_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_1(1))
        self.minArea_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_2(1))
        self.maxArea_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_3(1))
        self.minCircularity_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_4(100))
        self.maxCircularity_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_5(100))
        self.minConvexity_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_6(100))
        self.maxConvexity_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_7(100))
        self.minInertiaRatio_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_8(100))
        self.maxInertiaRatio_horizontalSlider.valueChanged.connect(lambda: self.ParamUpdated_9(100))
        # Connect Save and Load Config button
        self.SaveConfig_Button.clicked.connect(self.SaveConfig)
        self.LoadConfig_Button.clicked.connect(self.LoadConfig)

    @pyqtSlot()
    # Function to update Textedit with value of Sliderbar
    def TexteditUpdated(self, Slider_obj, Textedit_obj, divider):
        Textedit_obj.setText(str(Slider_obj/divider))
 
    # Functions to update Param of algorithm with value of Sliderbar
    def ParamUpdated(self, divider):
        self.Alg.SimpleBlobDetector_params.minThreshold = (self.minThreshold_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_1(self, divider):
        self.Alg.SimpleBlobDetector_params.maxThreshold = (self.maxThreshold_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_2(self, divider):
        self.Alg.SimpleBlobDetector_params.minArea = (self.minArea_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_3(self, divider):
        self.Alg.SimpleBlobDetector_params.maxArea = (self.maxArea_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_4(self, divider):
        self.Alg.SimpleBlobDetector_params.minCircularity = (self.minCircularity_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_5(self, divider):
        self.Alg.SimpleBlobDetector_params.maxCircularity = (self.maxCircularity_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_6(self, divider):
        self.Alg.SimpleBlobDetector_params.minConvexity = (self.minConvexity_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_7(self, divider):
        self.Alg.SimpleBlobDetector_params.maxConvexity = (self.maxConvexity_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_8(self, divider):
        self.Alg.SimpleBlobDetector_params.minInertiaRatio = (self.minInertiaRatio_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
    def ParamUpdated_9(self, divider):
        self.Alg.SimpleBlobDetector_params.maxInertiaRatio = (self.maxInertiaRatio_horizontalSlider.value()/divider)
        self.Alg.RunBlobDetectionAlg()
        
    # Function: change chosen algorithm
    def AlgChanged(self):
        self.Alg_chosen = self.BlobDetection_comboBox.currentText()

    #  Function: Save current config
    def SaveConfig(self):
        self.Savedata = \
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.minThreshold) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.maxThreshold) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.minArea) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.maxArea) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.minCircularity) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.maxCircularity) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.minConvexity) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.maxConvexity) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.minInertiaRatio) +"\r"+\
             "{:.2f}".format(self.Alg.SimpleBlobDetector_params.maxInertiaRatio)
        # Rewrite file config
        f = open(".\BlobDetection\Config.txt", "w")
        f.write(self.Savedata)
        f.close()
        QMessageBox.about(self, "Save config", "Save config successfully")
    
    def LoadConfig(self):
        try:
            file1 = open(".\BlobDetection\Config.txt", "r")
        except:
            print("Cannot read save config file ")
        Read_data = file1.readlines()
        for i in range(10):
            Read_data[i] = Read_data[i].replace("\n", "")
        print(Read_data)
        self.Alg.SimpleBlobDetector_params.minThreshold = float(Read_data[0])
        self.Alg.SimpleBlobDetector_params.maxThreshold = float(Read_data[1])
        self.Alg.SimpleBlobDetector_params.minArea = float(Read_data[2])
        self.Alg.SimpleBlobDetector_params.maxArea = float(Read_data[3])
        self.Alg.SimpleBlobDetector_params.minCircularity = float(Read_data[4])
        self.Alg.SimpleBlobDetector_params.maxCircularity = float(Read_data[5])
        self.Alg.SimpleBlobDetector_params.minConvexity = float(Read_data[6])
        self.Alg.SimpleBlobDetector_params.maxConvexity = float(Read_data[7])
        self.Alg.SimpleBlobDetector_params.minInertiaRatio = float(Read_data[8])
        self.Alg.SimpleBlobDetector_params.maxInertiaRatio = float(Read_data[9])

        self.minThreshold_textEdit.setText(Read_data[0])
        self.maxThreshold_textEdit.setText(Read_data[1])
        self.minArea_textEdit.setText(Read_data[2])
        self.maxArea_textEdit.setText(Read_data[3])
        self.minCircularity_textEdit.setText(Read_data[4])
        self.maxCircularity_textEdit.setText(Read_data[5])
        self.minConvexity_textEdit.setText(Read_data[6])
        self.maxConvexity_textEdit.setText(Read_data[7])
        self.minInertiaRatio_textEdit.setText(Read_data[8])
        self.maxInertiaRatio_textEdit.setText(Read_data[9])

        self.minThreshold_horizontalSlider.setValue(int(float(Read_data[0])))
        self.maxThreshold_horizontalSlider.setValue(int(float(Read_data[1])))
        self.minArea_horizontalSlider.setValue(int(float(Read_data[2])))
        self.maxArea_horizontalSlider.setValue(int(float(Read_data[3])))
        self.minCircularity_horizontalSlider.setValue(int(float(Read_data[4])*100))
        self.maxCircularity_horizontalSlider.setValue(int(float(Read_data[5])*100))
        self.minConvexity_horizontalSlider.setValue(int(float(Read_data[6])*100))
        self.maxConvexity_horizontalSlider.setValue(int(float(Read_data[7])*100))
        self.minInertiaRatio_horizontalSlider.setValue(int(float(Read_data[8])*100))
        self.maxInertiaRatio_horizontalSlider.setValue(int(float(Read_data[9])*100))



