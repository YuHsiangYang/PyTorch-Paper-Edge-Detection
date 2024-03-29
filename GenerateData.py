import os
from datetime import datetime as time
import cv2
import tkinter.messagebox as tk
import numpy as np
import pandas as pd
import functions
from dataset import datasetStructure


data_root_dir = 'data'

circle_radius = 3
circle_thickness = 2

def update_img(window_name, image):
    cv2.imshow(window_name, image)

corners_index = np.array([0, 3, 6, 9])
current_point = 0
coordinates_collection = np.zeros((12, 2), dtype=np.int32)
points_temp = np.zeros((12, 2), dtype=np.int32)
current_image_done = False


def mouse_handler(event, x, y, flags, arguments):
    global corners_index
    global current_point
    global points_temp
    global current_image_done
    image_duplicated = arguments["image_object"].copy()

    # To set a circle following the mouse
    cv2.circle(image_duplicated, (x, y), circle_radius, (255, 0, 0), circle_thickness)
    update_img('image', image_duplicated)

    # Calculate the two points between the last point and the current position of the cursor
    if current_image_done == False:
        if event == cv2.EVENT_LBUTTONDOWN and np.array_equal(points_temp[0], [0, 0]):
            points_temp[corners_index[current_point]] = [x, y]
            current_point = 1
        elif current_point > 0 and (event == cv2.EVENT_MOUSEMOVE or event == cv2.EVENT_LBUTTONDOWN):
            if event == cv2.EVENT_LBUTTONDOWN:
                points_temp[corners_index[current_point]
                            ] = np.copy(np.array([x, y]))
                if current_point == 3:
                    current_image_done = True
                    points_temp[corners_index[current_point]+1:corners_index[current_point] + 3] = functions.calculate_interval(points_temp[corners_index[current_point]], points_temp[0])
                    tk.showinfo('Notice', 'Please click the next image')

                    # Save the points to the file
                    pandas_dataframe = pd.DataFrame(points_temp)
                    # Remove NaN values
                    pandas_dataframe = pandas_dataframe.dropna()
                    print(pandas_dataframe)
                    pandas_dataframe.reset_index(inplace=True)
                    pandas_dataframe = pandas_dataframe.iloc[:, :3]
                    pandas_dataframe.columns = ['index', 'x', 'y']
                    pandas_dataframe.to_csv(
                        os.path.join(arguments["label_base_path"], arguments["image_name"][:-4] + '.csv'), index=False)
                    current_point = 0
                current_point = current_point + 1
            elif event == cv2.EVENT_MOUSEMOVE:
                points_temp[corners_index[current_point] - 2:corners_index[current_point]] = functions.calculate_interval(points_temp[corners_index[current_point] - 3], [x, y])
    # Display the points on the image
    for i in range(0, len(points_temp)):
        if not np.array_equal(i, [0, 0]):
            cv2.circle(image_duplicated, tuple(points_temp[i]), circle_radius, (0, 0, 255), circle_thickness)
            update_img('image', image_duplicated)


start = time.now()

for key in datasetStructure:
    directory_path = datasetStructure[key]
    image_dir = directory_path[0]
    label_dir = directory_path[1]
    #[0] represents the image directory, [1] represents the label directory
    # Get all the files in the directory
    for image_name in os.listdir(os.path.join(image_dir)):
        #check if there is a label file for the image
        if os.path.exists(os.path.join(label_dir, image_name[:-4] + '.csv')):
            continue
        image_original = cv2.imread(os.path.join(image_dir, image_name))
        resized_image = functions.rescale_image(image_original)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 600, 600)
        cv2.imshow('image', resized_image)
        cv2.setMouseCallback('image', mouse_handler,
                             {
                                 "coordinate": coordinates_collection,
                                 "image_object": resized_image,
                                 "image_name": image_name,
                                 "label_base_path": label_dir})
        cv2.waitKey(0)
        points_temp = np.zeros((12, 2), dtype=np.int32)
        current_point = 0
        current_image_done = False
        print(image_name)

    print(dir)

end = time.now()
print("Time elapsed: {}".format(end - start))
