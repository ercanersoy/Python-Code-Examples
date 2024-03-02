# Video Capture - An simple video capture program
# Copyright (c) 2024 Ercan Ersoy
# This file licensed under MIT License.
# Write this code using ChatGPT and GitHub CoPilot.

# Imports
import cv2
import sys

# Initialize video capture
capture = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not capture.isOpened():
    # Print error message
    print("Error: Could not open webcam.", file=sys.stderr)

    # Exit the program
    exit()

# Continuously capture frames
while True:
    # Read the frame
    ret, frame = capture.read()
    
    # If frame is not read correctly
    if not ret:
        print("Error: Failed to capture frame.", file=sys.stderr)
        exit()

    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Wait for a key press
    key_code = cv2.waitKey(1)

    # Break the loop if ESC is pressed
    if cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the video capture object
capture.release()

# Close windows
cv2.destroyAllWindows()
