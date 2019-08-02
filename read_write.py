#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 01:36:53 2019

@author: akash
"""

import cv2

img=cv2.imread('lena.jpg',0)
(height,width) = img.shape
for i in range(0,height/2):
    for j in range(0,width):
        (img[i][j],img[height-1-i][width-1-j])=(img[height-1-i][width-1-j],img[i][j])
cv2.imshow('LENA',img)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite('duplicate.jpg',img)
    cv2.destroyAllWindows()