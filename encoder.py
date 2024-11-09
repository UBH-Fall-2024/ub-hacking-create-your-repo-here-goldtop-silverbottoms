import face_recognition
import numpy as np

# Parameters
num_images = 10  # Number of images to encode

# List to store face encodings
face_encodings_list = []

# Load and encode each image
for i in range(num_images):
    filename = f"known_image_{i+1}.jpg"
    print(f"Processing {filename}")
    
    # Load the image
    image = face_recognition.load_image_file(filename)
    
    # Get the face encoding
    face_encodings = face_recognition.face_encodings(image)
    
    if face_encodings:
        face_encodings_list.append(face_encodings[0])
        print(f"Encoding for {filename} captured")
    else:
        print(f"No face detected in {filename}")

# Ensure we have enough encodings to average
if len(face_encodings_list) < num_images:
    print("Insufficient face encodings captured. Try again.")
    exit()

# Average the encodings to create a single robust encoding
known_face_encoding = np.mean(face_encodings_list, axis=0)
print("Known face encoding generated by averaging multiple images.")

# Save the encoding to a file
np.save("known_face_encoding.npy", known_face_encoding)
print("Known face encoding saved as 'known_face_encoding.npy'.")