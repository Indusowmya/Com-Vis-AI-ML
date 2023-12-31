import cv2
import numpy as np

# Load two images
image1 = cv2.imread(r"E:\N.INDU SOWMYA\TCE in lab Internship\Quantanics\intern program\com vis\Tig.jpg")
image2 = cv2.imread(r"E:\N.INDU SOWMYA\TCE in lab Internship\Quantanics\intern program\com vis\ora.jpg")

# Check if images were loaded successfully
if image1 is None or image2 is None:
    print("Error loading images.")
    exit()

# Resize the images to the same dimensions (optional)
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Perform bitwise XOR operation
result = cv2.bitwise_xor(image1, image2)

# Display the original images and the result
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise XOR Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
