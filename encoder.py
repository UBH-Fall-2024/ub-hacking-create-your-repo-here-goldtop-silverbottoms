import face_recognition
import numpy as np
import os

# Parameters
num_images = 30  # Target number of images to encode
min_encodings = 18  # Minimum number of encodings needed to proceed
known_dir = "known"  # Directory containing the known images

# List to store face encodings
face_encodings_list = []

# Load and encode each image in the "known" folder
for i in range(num_images):
    filename = os.path.join(known_dir, f"known_image_{i+1}.jpg")
    print(f"Processing {filename}")

    # Load the image
    image = face_recognition.load_image_file(filename)

    # Get the face encoding
    face_encodings = face_recognition.face_encodings(image)

    if face_encodings:
        face_encodings_list.append(face_encodings[0])
        print(f"Encoding for {filename} captured")
    else:
        print(f"No face detected in {filename}. Skipping this image.")

# Ensure we have enough encodings to proceed
if len(face_encodings_list) < min_encodings:
    print(f"Only {len(face_encodings_list)} encodings captured, which is below the minimum required of {min_encodings}. Try capturing more images.")
    exit()

# Average the encodings to create a single, robust encoding
known_face_encoding = np.mean(face_encodings_list, axis=0)
print("Known face encoding generated by averaging multiple images.")

# Save the encoding to a file
np.save("known_face_encoding.npy", known_face_encoding)
print("Known face encoding saved as 'known_face_encoding.npy'.")
