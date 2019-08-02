#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:45:20 2019

@author: akash
"""

import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img,(x,y),3,(255,0,0),-1)
            points.append((x,y))
            if len(points)>=2:
                cv2.line(img,points[-1],points[-2],(255,0,0),5)
            cv2.imshow('POINTS CONNECTOR',img)

img=cv2.imread('black_board.jpg')
points=[]
cv2.imshow('POINTS CONNECTOR',img)
cv2.setMouseCallback('POINTS CONNECTOR',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()