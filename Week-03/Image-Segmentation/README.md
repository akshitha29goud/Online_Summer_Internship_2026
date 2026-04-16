#  Week 03 - Image Segmentation using YOLO

---

##  Task Description

Performed semantic segmentation on images extracted from video using YOLOv8 segmentation model. Generated segmented images, converted them into a video, and added background audio.

---

##  Model Used

YOLOv8 segmentation model (`yolov8n-seg.pt`)

---

##  Code Files

- segment_images.py
- generate_metrics.py

---

##  Commands Used

### Run segmentation:
python segment_images.py

### Generate video:
ffmpeg -framerate 30 -i seg_output/frame-%04d.jpg -c:v libx264 seg_video.mp4

### Add audio:
ffmpeg -i seg_video.mp4 -i audio.mp3 -c:v copy -c:a aac final_seg_video.mp4

### Generate metrics:
python generate_metrics.py

---

##  Output Video

https://drive.google.com/file/d/1ckPopTcPp_g6J5dz_j5T45ulbBw3aLkg/view?usp=sharing

---

##  Performance Metrics

https://drive.google.com/file/d/1awKROFBrtP2cx_ZUfNMPjnnkFBXR03dm/view?usp=sharing

---

##  Observation

The model was trained for only 1 epoch on a small dataset, so precision, recall, and mAP values are very low. This is expected behavior.

Segmentation provides pixel-level classification of objects.
