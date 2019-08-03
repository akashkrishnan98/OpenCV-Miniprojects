#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 06:02:15 2019

@author: akash
"""

import cv2

apples=cv2.imread('apple.jpg')
oranges=cv2.imread('orange.jpg')
img1=cv2.resize(apples,(400,400))
img2=cv2.resize(oranges,(400,400))

#horned apple
stem=apples[ 0:100,150:230]
apples[0:100,250:330]=stem

#dest=cv2.add(img1,img2)
dest=cv2.addWeighted(apples,0.5,oranges,0.5,1)
cv2.imwrite('apples_and_oranges.jpg',dest)
cv2.imshow('APPLES AND ORANGES',dest)
cv2.waitKey(0)
cv2.destroyAllWindows()