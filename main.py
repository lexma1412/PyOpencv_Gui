import numpy as np
import cv2
from matplotlib import pyplot as plt

def main():
    cv2.namedWindow("aaa")
    cap = cv2.VideoCapture("Highway.mp4") 
    backSub = cv2.createBackgroundSubtractorMOG2()
    while cap.isOpened():
        ret, frame = cap.read()
        # Apply background subtraction
        fg_mask = backSub.apply(frame)
        # # Find contours
        # contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # # print(contours)
        # frame_ct = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
        # # apply global threshold to remove shadows
        # retval, mask_thresh = cv2.threshold( fg_mask, 1, 255, cv2.THRESH_BINARY)
        # # set the kernal
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        # # Apply erosion
        # mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)
        # min_contour_area = 100  # Define your minimum area threshold
        # large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
        # frame_out = frame.copy()
        # for cnt in large_contours:
        #     x, y, w, h = cv2.boundingRect(cnt)
        #     frame_out = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 200), 3)
        cv2.imshow("aaa",fg_mask)
        cv2.waitKey(5)

    while True:
        k = cv2.waitKey(0) & 0xFF
        print(k)
        if k == 27:
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()