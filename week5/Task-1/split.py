import os
import random
import shutil

source = "frames"

train_dir = "dataset/images/train"
val_dir = "dataset/images/val"

images = os.listdir(source)
random.shuffle(images)

split = int(len(images) * 0.8)

train_images = images[:split]
val_images = images[split:]

for img in train_images:
    shutil.copy(os.path.join(source, img), os.path.join(train_dir, img))

for img in val_images:
    shutil.copy(os.path.join(source, img), os.path.join(val_dir, img))

print("Dataset split completed!")