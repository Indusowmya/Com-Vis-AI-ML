import cv2

# Load an image
image = cv2.imread(r"E:\N.INDU SOWMYA\TCE in lab Internship\Quantanics\intern program\com vis\Dog.png")

# Apply bilateral filter
blurred_image = cv2.bilateralFilter(image, 9, 75, 75)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
