#  Object Detection on Multiple Images

---

##  Task Description

Applied YOLO object detection on multiple images extracted from a video and created a video from detected frames.

---

##  Model Used

YOLOv8 pretrained model

---

##  Python Code

from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir():
    if file.endswith(".jpg"):
        results = model(file)
        results[0].save(filename=os.path.join(output_folder, file))

print("Done!")

---

##  Commands Used

### Run detection:
python detect_images.py

### Convert images to video:
ffmpeg -framerate 30 -i output/frame-%04d.jpg -c:v libx264 detected_video.mp4

### Add audio:
ffmpeg -i detected_video.mp4 -i audio.mp3 -c:v copy -c:a aac final_video.mp4

---

##  Output Video

https://drive.google.com/file/d/1rtDoM39cvIQJAhk2Rpry02BTOyv53lcB/view?usp=sharing

---

##  Observation

YOLO detects only objects trained on COCO dataset such as person, car, etc.

in week1 the video contains flowers. Since YOLO is pretrained on COCO dataset,
it does not detect flowers. So I used another video.
