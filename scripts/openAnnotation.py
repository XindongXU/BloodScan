import json
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load JSON annotation file
class_name = 'class1'
folder_path = './data/rawdata/' + class_name + '/'
json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]
numb_files = np.random.randint(0, len(json_files))

with open(folder_path + json_files[numb_files], 'r') as f:
    data = json.load(f)

# Load image paths
image_path_normal = data["imagePath"]
image_path_blue   = data["imagePath"]

if class_name == 'class1':
    image_path_normal = image_path_normal.replace("T5", "T3").rsplit("_", 1)[0] + f"_{int(image_path_normal.rsplit('_', 1)[1].split('.')[0]) - 2}.bmp"
elif class_name == 'class2':
    image_path_blue = image_path_blue.replace("T3", "T5").rsplit("_", 1)[0] + f"_{int(image_path_blue.rsplit('_', 1)[1].split('.')[0]) + 2}.bmp"

image_normal = cv2.imread(folder_path + image_path_normal)
image_blue   = cv2.imread(folder_path + image_path_blue)
image_normal = cv2.cvtColor(image_normal, cv2.COLOR_BGR2RGB)
image_blue   = cv2.cvtColor(image_blue, cv2.COLOR_BGR2RGB)

# Extract and draw points on both images
for shape in data["shapes"]:
    points = shape["points"][0]  # Get the first point from the "points" array
    label = shape["label"]
    x, y = int(points[0]), int(points[1])

    cv2.circle(image_normal, (x, y), radius=8, color=(255, 0, 0), thickness=-1)  # Red circle
    cv2.putText(image_normal, label, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Green text
    cv2.circle(image_blue, (x, y), radius=8, color=(255, 0, 0), thickness=-1)  # Red circle
    cv2.putText(image_blue, label, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Green text

# Display both annotated images
plt.figure(figsize=(20, 10))

plt.subplot(1, 2, 1)
plt.imshow(image_normal)
plt.axis("off")
plt.title("Annotated Normal Image")

plt.subplot(1, 2, 2)
plt.imshow(image_blue)
plt.axis("off")
plt.title("Annotated Blue Image")

plt.show()