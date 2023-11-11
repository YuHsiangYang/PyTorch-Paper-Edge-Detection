import unittest
import numpy as np
import cv2
from GenerateData import rescale_image

class TestRescaleImage(unittest.TestCase):
    def test_rescale_image(self):
        # Create a dummy image of size 800x600
        image = np.zeros((800, 600, 3))

        # Call the function to resize the image
        resized_image = rescale_image(image)

        # Check if the resized image size is 384x288 (maintaining aspect ratio)
        self.assertEqual(resized_image.shape[0], 288)
        self.assertEqual(resized_image.shape[1], 384)

if __name__ == '__main__':
    unittest.main()