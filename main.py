import numpy as np
import cv2
from matplotlib import pyplot as plt

def main():
    cv2.namedWindow("aaa")
    cv2.waitKey(5)

    while True:
        k = cv2.waitKey(0) & 0xFF
        print(k)
        if k == 27:
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()