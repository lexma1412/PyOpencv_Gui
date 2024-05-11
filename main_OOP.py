import cv2
import numpy as np;
import time
from timeit import default_timer as timer
import sys
import PySide2
#from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from MainWindow_Gui import MyMainWindow


def main():
    print("Hello\r\n")
    # Create instance with class BlobDetection
    #SimpleBlobDetect_obj = BlobDetection("blob_test.png", "SimpleBlobDetect")
    # Run Blob Detection algorithm
    #start = timer()
    #SimpleBlobDetect_obj.RunBlobDetection()
    #end = timer()
    #print("SimpleBlobDetect Execution time: %f (ms)",(end - start)/1000) # Time in seconds
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
    while(1):
         k = cv2.waitKey(1) & 0xFF
         if k == 27:
             break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()