import numpy as np
import cv2
from matplotlib import pyplot as plt

def main():
    img = cv2.imread("test_img.png",cv2.IMREAD_GRAYSCALE)
    out_img = cv2.Laplacian(img, cv2.CV_64F)
    out_img = cv2.convertScaleAbs(out_img)
    for e in out_img:
        print(e)
    cv2.namedWindow("aaa")
    cv2.imshow("aaa", out_img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()