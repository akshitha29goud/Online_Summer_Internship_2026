import cv2
import os
import re

# Folder containing frames
folder = "frames"

# Get all image files
files = os.listdir(folder)

# Sort by number in filename
def get_number(f):
    match = re.search(r'(\d+)', f)
    return int(match.group(1)) if match else 0

files = sorted(files, key=get_number)

# Read first valid frame
first_frame = cv2.imread(os.path.join(folder, files[0]))

if first_frame is None:
    print("Error: Cannot read images")
    exit()

height, width, _ = first_frame.shape

# FIX: define codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# LOW FPS = longer video
fps = 2

video = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

# OPTIONAL: repeat frames to make video longer
repeat_each_frame = 3

for file in files:
    path = os.path.join(folder, file)
    frame = cv2.imread(path)

    if frame is None:
        continue

    for _ in range(repeat_each_frame):
        video.write(frame)

video.release()

print("Video created successfully: output.mp4")