import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt

def load_images(data_dir):
    X = []
    y = []
    labels = {"non_fall": 0, "fall": 1}

    for label_name in labels:
        folder = os.path.join(data_dir, label_name)
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                img = cv2.imread(file_path)
                img = cv2.resize(img, (64, 64)) 
                img_flat = img.flatten()        
                X.append(img_flat)
                y.append(labels[label_name])
            except:
                print(f"Error loading {file_path}")
    return np.array(X), np.array(y)

X, y = load_images('dataset')
print(f"Loaded {len(X)} images.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
plt.imshow(cm, cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.xticks([0, 1], ['Non-Fall', 'Fall'])
plt.yticks([0, 1], ['Non-Fall', 'Fall'])
plt.show()

joblib.dump(model, 'fall_detection_model.pkl')
print("Model saved as fall_detection_model.pkl")
