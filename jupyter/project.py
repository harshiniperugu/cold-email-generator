import os
import cv2
import matplotlib.pyplot as plt

# Set the dataset path
dataset_path = r"C:\Users\harsh\Downloads\SROIE-datasetv2-main\SROIE-datasetv2-main\train\img"

# List all image files
image_files = [f for f in os.listdir(dataset_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Display some sample images
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
for i, ax in enumerate(axes.flat):
    img_path = os.path.join(dataset_path, image_files[i])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    ax.imshow(img)
    ax.set_title(image_files[i])
    ax.axis("off")

plt.show()
