import cv2
import numpy as np;
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
img =""
def SimpleBlobDetect(x):
    global img
    # Set up the SimpleBlobDetector with default parameters
    params = cv2.SimpleBlobDetector_Params()
    #Set the threshold
    params.minThreshold = cv2.getTrackbarPos("minThreshold","SimpleBlobDetect")
    params.maxThreshold = cv2.getTrackbarPos("maxThreshold","SimpleBlobDetect")

    # Set the area filter
    params.filterByArea = True
    params.minArea = cv2.getTrackbarPos("minArea","SimpleBlobDetect")
    params.maxArea = 5000.0

    # Set the circularity filter
    params.filterByCircularity = True
    params.minCircularity = 0.1
    params.maxCircularity = 1

    # Set the convexity filter
    params.filterByConvexity = True
    params.minConvexity = 0.87
    params.maxConvexity = 1

    # Set the inertia filter
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    params.maxInertiaRatio = 1

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs
    keypoints = detector.detect(img)

    # Draw detected blobs as red circles
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # Show the image with detected blobs
    cv2.imshow("SimpleBlobDetect", img_with_keypoints)

def GassianBlobDetect():
    # Apply Laplacian of Gaussian
    blobs_log = cv2.Laplacian(img, cv2.CV_64F)
    blobs_log = np.uint8(np.absolute(blobs_log))
        
    # Set up the detector with default parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 100
    params.maxThreshold = 200

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 100

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.9

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.2

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(blobs_log)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of the blob
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)

def main():
    print("Hello")
    global img
    # Load image
    img = cv2.imread("blob_test.png", cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow("SimpleBlobDetect")
    cv2.createTrackbar("minThreshold","SimpleBlobDetect",0,255,SimpleBlobDetect)
    cv2.createTrackbar("maxThreshold","SimpleBlobDetect",0,255,SimpleBlobDetect)
    cv2.createTrackbar("minArea","SimpleBlobDetect",100,255,SimpleBlobDetect)
    cv2.createTrackbar("maxArea","SimpleBlobDetect",1000,2000,SimpleBlobDetect)
    SimpleBlobDetect(0)
    GassianBlobDetect()
    while(1):
         k = cv2.waitKey(1) & 0xFF
         if k == 27:
             break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
