import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject
import time
# Video State:
# 1 = Run
# 2 = Pause
high_frame = 854
width_frame = 480
channel_frame = 3
class VideoCapture(QThread):
    # Signal emitted when a new image or a new frame is ready.
    FrameUpdated = pyqtSignal(QImage)

    def __init__(self, video_path, VideoCaptureAlg):
        super(VideoCapture, self).__init__()
        self.VidState = 2 # Pause
        self.Video = cv2.VideoCapture(video_path)
        self.fps=0
        self.cur_time=0
        self.prev_time=0
        self.processAlg = VideoCaptureAlg
        self.backSub = cv2.createBackgroundSubtractorMOG2()
        
    # Ref: https://github.com/god233012yamil/Streaming-IP-Cameras-Using-PyQt-and-OpenCV/blob/main/Streaming_IP_Camera_Using_PyQt_OpenCV.py#L145
    def run(self)-> None:
        # Run state
        while(1):
            if (self.VidState==1):
                #self.cur_time = time.time()
                #print(start)
                ret, frame = self.Video.read()
                # If frame is read correctly.
                if ret:
                    # Call function to process any algorithm
                    #frame = self.FrameProcess(1, frame)
                    #backSub = cv2.createBackgroundSubtractorMOG2()
                    # Apply background subtraction
                    fg_mask = self.backSub.apply(frame)
                
                    # Find contours
                    contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    # print(contours)
                    frame_ct = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
                    # apply global threshold to remove shadows
                    retval, mask_thresh = cv2.threshold( fg_mask, 1, 255, cv2.THRESH_BINARY)
                    # set the kernal
                    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
                    # Apply erosion
                    mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)
                    min_contour_area = 100  # Define your minimum area threshold
                    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
                    #frame_out = frame.copy()
                    for cnt in large_contours:
                        x, y, w, h = cv2.boundingRect(cnt)
                        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 200), 3)
                    # Get the frame height, width and channels.
                    height, width, channels = frame.shape
                    # Calculate the number of bytes per line.
                    bytes_per_line = width * channels
                    # Convert image from BGR (cv2 default color format) to RGB (Qt default color format).
                    cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    #Convert the image to Qt format.
                    qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                    # If this is the case, call instead: qt_rgb_image.scaled(1280, 720) 
                    qt_rgb_image_scaled = qt_rgb_image.scaled(high_frame, width_frame, Qt.KeepAspectRatio)  # 720p
                    # Emit this signal to notify that a new image or frame is available.
                    #end = time.time()
                    self.cur_time = time.time()
                    if(self.cur_time-self.prev_time) != 0 :
                        self.fps = 1.0/(self.cur_time-self.prev_time)
                    self.prev_time = self.cur_time
                    self.FrameUpdated.emit(qt_rgb_image_scaled)
                else:
                    self.Video.release()
                    self.VidState=3
                    print("Run Video Fail")
            # Pause state
            elif (self.VidState==3): break
    
    def FrameProcess(self, processAlg, frame):
        if (processAlg == 1):
           outframe = self.BackgroundSubtractObjectDetection(frame)
        return outframe

    def BackgroundSubtractObjectDetection(self, frame):
        # Apply background subtraction
        fg_mask = self.backSub.apply(frame)
       
        # Find contours
        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)
        frame_ct = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
        # apply global threshold to remove shadows
        retval, mask_thresh = cv2.threshold( fg_mask, 180, 255, cv2.THRESH_BINARY)
        # set the kernal
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        # Apply erosion
        mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)
        min_contour_area = 500  # Define your minimum area threshold
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
        frame_out = frame.copy()
        for cnt in large_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            frame_out = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 200), 3)
        return frame_out

        