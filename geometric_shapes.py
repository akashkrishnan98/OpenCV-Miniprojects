#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:49:22 2019

@author: akash
"""

import cv2

img=cv2.imread('lena.jpg',1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.arrowedLine(gray,(0,gray.shape[0]/2),(gray.shape[1]/2,gray.shape[0]/2),(0,0,0),7)
gray=cv2.rectangle(gray,(gray.shape[1]/4,0),(gray.shape[1]/2,gray.shape[0]/4),(0,0,0),-5)
gray=cv2.circle(gray,(gray.shape[1]*3/8,gray.shape[0]/8),gray.shape[1]/8,(255,255,255),5)
cv2.imwrite('geomentrix_shapes.jpg',gray)