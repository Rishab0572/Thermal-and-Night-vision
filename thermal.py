import cv2
import numpy as np

# Create VideoCapture object
cap = cv2.VideoCapture(0)  # Change to the index of your camera or provide the path to a video file

# Check if the camera/video is opened
if not cap.isOpened():
    print("Error: Could not open camera/video.")
    exit()

# Function to perform thermal processing on a single frame
def process_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform image processing (e.g., thresholding, filtering, etc.)
    # Example:
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    return thresh

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Perform thermal processing on the frame
    processed_frame = process_frame(frame)

    # Display the processed frame
    cv2.imshow('Thermal Scan', processed_frame)

    # Check for user input to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()