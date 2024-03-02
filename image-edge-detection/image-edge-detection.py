# Image Edge Detection - A simple image edge detection program
# Copyright (c) 2024 Ercan Ersoy
# This file licensed under MIT License.
# Write this code using ChatGPT and GitHub CoPilot.

# Imports
import cv2
import numpy as np
import sys

# Initialize video capture
capture = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not capture.isOpened():
    # Print error message
    print("Error: Could not open webcam.", file=sys.stderr)

    # Exit the program
    exit()

ret, image = capture.read()

# If frame is not read correctly
if not ret:
    # Print error message
    print("Error: Failed to capture frame.", file=sys.stderr)

    # Exit the program
    exit()

# Convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur to the image
image = cv2.medianBlur(image, 5)

# Define a kernel
kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

# Apply the kernel to the image
image = cv2.filter2D(image, -1, kernel)

# Apply Gaussian blur to the image
image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection to the image
image = cv2.Canny(image, 100, 200)

# Save the image
cv2.imwrite("image.jpg", image)
