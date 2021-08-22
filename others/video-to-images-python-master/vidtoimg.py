#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run this file in folder /AntiDrone/ 

import cv2

# Data folders
VIDEO_FOLDER = 'C:/Users/woosa/Desktop/'
IMAGE_FOLDER = 'C:/Users/woosa/Desktop/FourthOne/'

#filename = 'antidrone1_cut_2' # Mostly air view - TRAIN
#filename = 'antidrone1_cut_3' # Mostly air view - TRAIN
#filename = 'antidrone1_cut_4' # Mostly air view - TRAIN
#filename = 'antidrone2_cut_1' # Mostly air view -- leave for testing
#filename = 'antidrone3_cut_1' # Mostly ground view - TRAIN
#filename = 'antidrone3_cut_3' # ground view
#filename = 'antidrone5_cut_2' # air view
#filename = 'antidrone6_cut_1' # Poor quality ground view
filename = 'FHD0006' # Better quality ground view - TRAIN
#filename = 'antidrone6_cut_3' # Mixed view
#filename = 'antidrone6_cut_4' # Mostly air view

cap = cv2.VideoCapture(VIDEO_FOLDER + filename + '.MOV')

i = 0
while True:

    i = i + 1
    # Read a frame
    hasFrame, frame = cap.read()
    height, width, channels = frame.shape
    
    #frame = frame[int(height/2)-450:int(height/2)+450,int(width/2)-450:int(width/2)+450]
    
    # Check to see if we have reached the end of the stream
    if frame is None:
        break
    
    if i % 10 == 0:
        cv2.imwrite(IMAGE_FOLDER + filename + '_frame{}.jpg'.format(i), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 98])
	
    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF 
                
	# If the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
 
    
    #if i == 500:
    #    break
    
cap.release()
cv2.destroyAllWindows()