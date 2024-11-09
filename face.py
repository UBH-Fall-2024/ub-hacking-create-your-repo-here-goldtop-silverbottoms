import cv2
import time
import os

# Parameters
num_images = 100  # Number of images to capture
frame_skip = 20  # Frames to skip for camera adjustment

# Directory to save known images
known_dir = "known"
os.makedirs(known_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Start the webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Unable to access the camera.")
    exit()

# Allow the camera to adjust to lighting
for _ in range(frame_skip):
    ret, _ = video_capture.read()
    if not ret:
        print("Failed to grab frame.")
        break

# Capture and save multiple images
for i in range(num_images):
    ret, frame = video_capture.read()
    if ret:
        # Save each captured image in the "known" directory
        filename = os.path.join(known_dir, f"known_image_{i+1}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Image {i+1} captured and saved as {filename}")
        time.sleep(0.1)  # Pause briefly between captures
    else:
        print(f"Failed to capture image {i+1}")

# Release the camera
video_capture.release()
cv2.destroyAllWindows()
