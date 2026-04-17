#  Week 03 - Video Stacking (Task 2)

---

##  Task Description

Combined three videos:
- Raw video (generated from frames)
- Object Detection video (bounding boxes)
- Segmentation video (colored masks)

Stacked them vertically using FFmpeg and added a new audio track.

---

##  Concept

- Detection shows bounding boxes around objects.
- Segmentation highlights objects using pixel-level masks.

---

##  Commands Used

### Create raw video:
ffmpeg -framerate 30 -i frame-%04d.jpg -c:v libx264 -pix_fmt yuv420p raw.mp4

### Stack videos:
ffmpeg -i raw.mp4 -i detected_video.mp4 -i seg_video.mp4 -filter_complex "vstack=inputs=3" -an stacked.mp4

### Add audio:
ffmpeg -i stacked.mp4 -i audio.mp3 -c:v copy -c:a aac final_stacked_video.mp4

---

##  Final Output Video

https://drive.google.com/file/d/1CqoMawjf22DKwDKNf7BIySYUPlzVcSWE/view?usp=sharing

---

##  Observation

The output clearly shows the difference between:
- Raw video (original frames)
- Detection (bounding boxes)
- Segmentation (pixel-level masks)

Videos with objects like people and vehicles produced better results as they are part of the pretrained YOLO dataset.
