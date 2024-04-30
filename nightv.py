import cv2
import numpy as np


# Function to apply night vision effect
def night_vision(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Increase brightness (adjust this value as needed)
    brightened = cv2.add(gray, 50)

    # Apply adaptive histogram equalization for better contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(brightened)

    # Apply a green tint to simulate night vision
    green_tint = cv2.merge([np.zeros_like(enhanced), enhanced, np.zeros_like(enhanced)])

    return green_tint


# Create VideoCapture object
cap = cv2.VideoCapture(0)  # Change to the index of your camera or provide the path to a video file

# Check if the camera/video is opened
if not cap.isOpened():
    print("Error: Could not open camera/video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Apply night vision effect to the frame
    nv_frame = night_vision(frame)

    # Display the processed frame
    cv2.imshow('Night Vision', nv_frame)

    # Check for user input to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()