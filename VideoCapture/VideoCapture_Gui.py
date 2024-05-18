import cv2
import numpy as np;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject

from VideoCapture.ui_Qt_VideoCapture import Ui_VideoCapture_Gui
from VideoCapture.VideoCapture_Alg import *


class MyVideoCapture_Gui(QtWidgets.QWidget, Ui_VideoCapture_Gui):
    def __init__(self):
        super(MyVideoCapture_Gui, self).__init__()
        self.setupUi(self)
        self.FPS_label.setHidden(True)
        # Init algorithm object
        self.Alg = VideoCapture("Test_Video.mp4", None)
        # Connect thread
        self.Alg.FrameUpdated.connect(lambda image: self.ShowVideo(image))
        # Connect UI
        self.Start_pushButton.clicked.connect(self.RunVideo)
        self.Stop_pushButton.clicked.connect(self.PauseVideo)

        # Start thread
        self.Alg.start()

    @pyqtSlot()
    def ShowVideo(self, frame: QImage) -> None:
        self.Video_label.setPixmap(QPixmap.fromImage(frame))
        #self.FPS_label.setText(str(int(self.Alg.fps)))
        self.FPS_label.setText(QtCore.QCoreApplication.translate("VideoCapture_Gui", "<html><head/><body><p><span style=\" font-weight:600; color:#f80000;\">FPS: "+str(int(self.Alg.fps))+"</span></p></body></html>"))
        self.FPS_label.setHidden(False)
    
    @pyqtSlot()
    def RunVideo(self):
        # Set State to Run
        print("Start clicked")
        self.Alg.VidState = 1

    @pyqtSlot()
    def PauseVideo(self):
        # Set State to Pause
        print("Pause clicked")
        self.Alg.VidState = 2
    
     # Overwrite method closeEvent from class QWidget.
    def closeEvent(self, event) -> None:
        if self.Alg.isRunning():
            self.Alg.quit()
         # Accept the event
        event.accept()

