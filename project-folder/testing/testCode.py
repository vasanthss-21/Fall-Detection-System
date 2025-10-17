import cv2
import numpy as np
import joblib

model = joblib.load('fall_detection_model.pkl')

img_path = '22.jpg'
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found or path incorrect.")
    exit()

img = cv2.resize(img, (64, 64))
img_flat = img.flatten().reshape(1, -1)

result = model.predict(img_flat)

# 4. Print the result
if result[0] == 1:
    print("🔴 Fall Detected")
else:
    print("🟢 No Fall Detected")
