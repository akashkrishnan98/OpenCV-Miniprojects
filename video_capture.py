#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 07:08:59 2019

@author: akash
"""

import cv2

cap=cv2.VideoCapture('tree.avi')
frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('tree_out.avi',fourcc,30,(frame_width,frame_height))

while(cap.isOpened()):
        (ret, frame)=cap.read()
        if ret==True:
           
            out.write(frame)
        else:   
            break

cap.release()
out.release()
cv2.destroyAllWindows()
        
