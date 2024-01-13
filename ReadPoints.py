import pandas as pd
import cv2
import os
import functions
from dataset import datasetStructure

#[0] = images
#[1] = labels

images = os.listdir(datasetStructure["training"][0])
labels = os.listdir(datasetStructure["training"][1])
for i in range(0, len(images)):
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(os.path.join(datasetStructure["training"][1], labels[i]), index_col=0)
    df = df.dropna() #Remove the NaN values

    image = cv2.imread(os.path.join(datasetStructure["training"][0], images[i])) #Read the image
    image = functions.rescale_image(image)
    cv2.namedWindow('image')
    for i in range(0, len(df)):
        print("x: {} y:{}".format(df.loc[i, 'x'], df.loc[i, 'y']))
        cv2.circle(image, (df.loc[i, 'x'], df.loc[i, 'y']), 5, (0, 0, 255), 2)

    cv2.imshow('image', image)
    cv2.waitKey(0)