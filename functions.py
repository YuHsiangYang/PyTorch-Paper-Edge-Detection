import cv2
import numpy as np

def rescale_image(image):
    """
    Rescale an image to a target size while maintaining aspect ratio.
    
    ---
    Parameters
    ---
    image (np.array): The original image.
    
    ---
    Returns
    ---
    Matlike: The rescaled image.
    """
    target_size = (512, 512)
    #get the larger dimension of the image whether it is height or width
    larger_dimension = max(image.shape[0], image.shape[1])
    print(image.shape)

    #calculate the ratio of the larger dimension to the target dimension
    ratio = larger_dimension / target_size[0]
    #calculate the new dimension of the image
    new_dimension = (int(image.shape[0] / ratio), int(image.shape[1] / ratio))
    #resize the image
    resized_image = cv2.resize(image, new_dimension)
    return resized_image

def preprocess_image(image):
    """
    Preprocess an image by blurring it and converting it to grayscale.

    ---
    Parameters:
    ---
    image (np.array): The original image.
    
    ---
    Return:
    ---
    Matlike: The preprocessed image.
    """
    #blur the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    #convert the image to grayscale
    grayscale_blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
    return grayscale_blurred_image

def calculate_interval(point1, point2):
    """
    Calculate the interval between two points.

    ---
    Parameters:
    ---
    point1 (np.array): The first point.
    point2 (np.array): The second point.

    ---
    Returns:
    ---
    np.array: The interval between the two points with the shape (2, 2).
    """
    interval = np.zeros((2, 2), dtype=np.int32)
    #Calculate the difference between two points and multiply it by 0.333 and 0.667
    interval[0] = (point2 - point1) * 0.333 + point1
    interval[1] = (point2 - point1) * 0.667 + point1
    return interval
