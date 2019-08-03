#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 06:36:12 2019

@author: akash
"""

import cv2
import numpy as np

img1=np.zeros((400,400,3),np.uint8)
img2=np.zeros((400,400,3),np.uint8)

cv2.rectangle(img1,(0,0),(200,400),(255,255,255),-1)
cv2.rectangle(img2,(200,0),(400,400),(255,255,255),-1)

and_op=cv2.bitwise_and(img1,img2)
or_op=cv2.bitwise_or(img1,img2)
xor_op=cv2.bitwise_xor(img1,img2)

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('AND',and_op)
cv2.imshow('OR',or_op)
cv2.imshow('XOR',xor_op)
while True:
    key=cv2.waitKey(0)
    if key==ord('q') & 0xFF:
        cv2.destroyAllWindows()
        break
        
    

