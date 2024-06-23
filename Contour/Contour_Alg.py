import cv2
import numpy as np;

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

class FindContour:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        #Todo: manual threshold img to binary
        ret,self.binaryimg = cv2.threshold(self.img, 50, 255, 0)
        self.ContourMode = DictContourMode["RETR_LIST"]
        self.ContourMethod = DictContourMethod["CHAIN_APPROX_SIMPLE"]
        cv2.namedWindow("Image")
        cv2.imshow("Image", self.img)
    

    def FindContourAlg(self):
        contours, hehierarchy = cv2.findContours(self.binaryimg, self.ContourMode, self.ContourMethod)
        showimg = self.img.copy()
        cv2.drawContours(showimg, contours, -1, (50, 255, 0), 3)
        cv2.imshow("Image", showimg)
    