import cv2
import numpy as np;

class EdgeDetection:
    def __init__(self, img_path, EdgeDetectionAlg):
        self.org_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        self.hysteresislowth = 1
        self.hysteresishighth = 100
        self.Kernelsize = 3
        self.L2Grad = False
        cv2.namedWindow("Original Image")
        cv2.namedWindow("CannyEdge Image")
    
    def RunCannyEdgeAlg(self):
        edges = cv2.Canny(self.org_img,self.hysteresislowth,self.hysteresishighth,None,self.Kernelsize,self.L2Grad)
        cv2.imshow("Original Image", self.org_img)
        cv2.imshow("CannyEdge Image", edges)