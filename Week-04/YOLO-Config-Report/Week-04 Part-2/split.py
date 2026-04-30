import os, random, shutil

source = "images"
train_dir = "dataset/images/train"
val_dir = "dataset/images/val"
test_dir = "dataset/images/test"

images = os.listdir(source)
random.shuffle(images)

train = images[:100]
val = images[100:140]
test = images[140:]

def move(files, dest):
    for f in files:
        shutil.copy(os.path.join(source, f), os.path.join(dest, f))

move(train, train_dir)
move(val, val_dir)
move(test, test_dir)

print("Dataset split done!")