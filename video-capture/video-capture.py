# video Capture - An simple video capture program
# Copyright (c) 2024 Ercan Ersoy
# This file licensed under MIT License.
# Write this code using ChatGPT.

# Imports
import cv2
import sys

# Initialize video capture
capture = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not capture.isOpened():
    print("Error: Could not open webcam.", file=sys.stderr)
    exit()

# Continuously capture frames
while True:
    # Read the frame
    ret, frame = capture.read()
    
    # If frame is read correctly ret is True
    if not ret:
        print("Error: Failed to capture frame.", file=sys.stderr)
        break

    # Display the frame
    cv2.imshow('Frame', frame)
    
    key_code = cv2.waitKey(1)

    # Break the loop if ESC is pressed
    if cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the video capture object
capture.release()

# Close windows
cv2.destroyAllWindows()
