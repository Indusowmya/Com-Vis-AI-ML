import cv2

# Load an image
image = cv2.imread(r"E:\N.INDU SOWMYA\TCE in lab Internship\Quantanics\intern program\com vis\Boat.png")

# Apply Gaussian blur with a kernel size of 5x5
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
