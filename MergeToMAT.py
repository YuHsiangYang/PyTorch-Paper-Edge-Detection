from dataset import datasetStructure
import scipy.io
import os
import pandas as pd
import numpy as np
from pathlib import Path

# Get a list of all image files in the directory
images = np.array(os.listdir(datasetStructure["training"][0]))
labels = np.array(os.listdir(datasetStructure["training"][1]))

# Initialize an empty dictionary
data_dict = {}

# Loop over each image file
for i in range(0, len(images)):
    # Trim the last 4 characters from the image name
    image_name = images[i][:-4]

    # Find the corresponding label
    label_index = np.where(labels == image_name + '.csv')[0]
    if label_index.size > 0:
        # Read the corresponding CSV file into a DataFrame
        df = pd.read_csv(os.path.join(datasetStructure["training"][1], labels[label_index[0]]), index_col=0)
        df = df.dropna()

        # Convert the DataFrame to a dictionary and add it to the main dictionary
        data_dict[image_name] = {'x': df['x'].values, 'y': df['y'].values}

# Write the main dictionary to a .mat file
print(data_dict)
scipy.io.savemat('training_Data_Labels.mat', data_dict)