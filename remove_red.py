import cv2
import numpy as np
import os

def partB():
    pic = cv2.imread('test_crop.jpg')
    cat = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
    LLR = ( 140, 17, 45)#RED HSV=(0,255,255)
    ULR = ( 180, 255, 255)
    maskR = cv2.inRange(cat, LLR, ULR)
    #cv2.imshow("red", maskR)
    contourR,h=cv2.findContours(maskR, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    print(h)
    cv2.drawContours(pic, contourR, -1, (0, 255, 0), 1)
    cv2.imshow("window", pic)
    cv2.waitKey(0);
    #cat[:,:,2] = 0
    #cat[:,:,1] = 0
    cv2.imwrite('test_nored.jpeg', pic)

partB()
