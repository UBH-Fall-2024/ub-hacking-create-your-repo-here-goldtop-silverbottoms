import cv2
import time

# Parameters
num_images = 10  # Number of images to capture
frame_skip = 20  # Frames to skip to allow camera adjustment

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
        # Save each captured image with a unique filename
        filename = f"known_image_{i+1}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image {i+1} captured and saved as {filename}")
        time.sleep(0.5)  # Pause between captures for adjustment
    else:
        print(f"Failed to capture image {i+1}")

# Release the camera
video_capture.release()
cv2.destroyAllWindows()
