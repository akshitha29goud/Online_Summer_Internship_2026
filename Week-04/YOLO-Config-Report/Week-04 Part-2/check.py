import os

image_dir = "dataset/images/train"
label_dir = "dataset/labels/train"

missing = []

for img in os.listdir(image_dir):
    label = img.replace(".jpg", ".txt")
    if not os.path.exists(os.path.join(label_dir, label)):
        missing.append(img)

print("Missing labels:", len(missing))