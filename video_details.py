#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:33:01 2019

@author: akash
"""

import cv2
cap=cv2.VideoCapture('tree.avi')
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('video_details.avi',fourcc,15,(width,height))
cap.set(3,width)
cap.set(4,height)
while cap.isOpened():
    (ret,frame)=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        
        text="Width: " + str(cap.get(3)) + "  Height: " + str(cap.get(4))
        cv2.putText(frame,text,(10,50),font,0.5,(0,0,255),1)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows
