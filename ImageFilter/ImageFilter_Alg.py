import cv2
import numpy as np;

class ImageFilter:
    def __init__(self, img_path, ImageFilterAlg):
        self.org_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        self.ChosenAlg = "GaussianFilter"
        #self.Kernelsize = 3
        #self.MedianKernelsize = 3
        cv2.namedWindow("Original Image")
        cv2.namedWindow("Processed Image")
    
    def RunGaussianFilterAlg(self, GaussKernelsize, SigmaX):
        process_img = cv2.GaussianBlur(self.org_img, (GaussKernelsize, GaussKernelsize), SigmaX)
        cv2.imshow("Original Image", self.org_img)
        cv2.imshow("Processed Image", process_img)
    
    def RunMedianFilterAlg(self, MedianKernelsize):
        process_img = cv2.medianBlur(self.org_img, MedianKernelsize)
        cv2.imshow("Original Image", self.org_img)
        cv2.imshow("Processed Image", process_img)
    
    def RunLaplacianFilterAlg(self,):
        process_img = cv2.Laplacian(self.org_img,cv2.CV_64F)
        cv2.imshow("Original Image", self.org_img)
        cv2.imshow("Processed Image", process_img)
