import torch
import os
from datetime import datetime as time
import cv2
import numpy as np

data_root_dir = 'data'


sides_index = 4
corners_index = np.array([0, 3, 6, 9])
current_corner = 0
coordinates_collection = np.zeros((8, 2), dtype=np.int32)

points_temp = np.zeros((8, 2), dtype=np.int32)

def mouse_handler(event, x, y, flags, points):
    global mosue_up
    global corners_index
    global current_corner
    global points_temp
    if points_temp[0][0] == 0 and points_temp[0][1] == 0:
        points_temp = np.array(points[0], copy=True)
    image = points[1]
    
    if event == cv2.EVENT_RBUTTONDOWN and current_corner == 0:
        points_temp[0] = np.array([x, y])
        print("right key pressed with ({})".format(points_temp[0]))
        
    if current_corner < sides_index:
        if event == cv2.EVENT_LBUTTONDOWN:
            # points_temp[corners_index[(current_corner+1)]] = (x, y)
            print(points_temp[0])
            cv2.line(image, points_temp[0], (x, y), (100, 0, 0), thickness=7)
            cv2.imshow('image', image)
            print("Mouse down")
            mouse_up = False
        if event == cv2.EVENT_LBUTTONUP:
            #Write the final points to the variable
            mouse_up = True
            current_corner += 1
        

start = time.now()
for dir in os.listdir(data_root_dir): # Get all the directories
    for file in os.listdir(os.path.join(data_root_dir, dir)): #Get all the files in the directory
        image_original = cv2.imread(os.path.join(data_root_dir, dir, file))
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 600, 600)
        cv2.imshow('image', image_original)
        cv2.setMouseCallback('image', mouse_handler, [coordinates_collection, image_original])
        cv2.waitKey(0)
        print(file)
end = time.now()
print("Time elapsed: {}".format(end - start))
