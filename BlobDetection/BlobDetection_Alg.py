import cv2
import numpy as np;

class BlobDetection:
    def __init__(self, img_path, BlobDetectAlg):
        # Read image from path as grayscale
        self.image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        # Set chosen algorithm
        self.SelectBlobDetectionAlg = BlobDetectAlg
        if (BlobDetectAlg == "SimpleBlobDetect"):
            # Set up the SimpleBlobDetector with default parameters
            self.SimpleBlobDetector_params = cv2.SimpleBlobDetector_Params()
            self.cvnameWindow = "SimpleBlobDetect"
            self.SimpleBlobDetector_params.minThreshold = 0
            self.SimpleBlobDetector_params.maxThreshold = 100
            self.SimpleBlobDetector_params.minArea = 1
            self.SimpleBlobDetector_params.maxArea = 5000
            # Set the circularity filter
            self.SimpleBlobDetector_params.filterByCircularity = True
            self.SimpleBlobDetector_params.minCircularity = 0.1
            self.SimpleBlobDetector_params.maxCircularity = 0.5
            # Set the convexity filter
            self.SimpleBlobDetector_params.filterByConvexity = True
            self.SimpleBlobDetector_params.minConvexity = 0.1
            self.SimpleBlobDetector_params.maxConvexity = 0.5
            # Set the inertia filter
            self.SimpleBlobDetector_params.filterByInertia = True
            self.SimpleBlobDetector_params.minInertiaRatio = 0.01
            self.SimpleBlobDetector_params.maxInertiaRatio = 1
            
        elif (self.SelectBlobDetectionAlg == "GassianBlobDetect"):
            self.cvnameWindow = "GassianBlobDetect"
        # TBD
        else: pass

        # function to run algorithm
    def RunBlobDetectionAlg(self):
        # Create a detector with the parameters
        detector = cv2.SimpleBlobDetector_create(self.SimpleBlobDetector_params)
        # Detect blobs
        keypoints = detector.detect(self.image)
        # Draw detected blobs as red circles
        img_with_keypoints = cv2.drawKeypoints(self.image, keypoints, np.array([]), (0, 0, 255),
                                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # Show the image with detected blobs
        cv2.imshow(self.cvnameWindow, img_with_keypoints)