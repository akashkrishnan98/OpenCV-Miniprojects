#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:06:43 2019

@author: akash
"""

import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    font=cv2.FONT_HERSHEY_SIMPLEX
    if event==cv2.EVENT_RBUTTONDOWN:
        strxy= str(x) + ', '+str(y)
        cv2.putText(img,strxy,(x,y),font,.5,(255,255,0),2)
        
    elif event==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        strBGR=str(blue)+ ", " + str(green)+ ", " + str(red)
        cv2.putText(img,strBGR,(x,y),font,.5,(255,0,0),2)
    cv2.imshow('MOUSE EVENT',img)
        
img=cv2.imread('lena.jpg')
cv2.imshow('MOUSE EVENT',img)
cv2.setMouseCallback('MOUSE EVENT',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
