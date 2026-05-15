# Week 5 - Overview

## Internship Tasks Completed

### WT1 - Dataset Creation and Annotation
- Extracted frames from video dataset
- Split dataset into train, validation and test sets
- Annotated objects using Label Studio
- Generated YOLO label files
- Created data.yaml, train.txt and val.txt files

### WT2 - Image Preprocessing
- Resized images using FFmpeg
- Preserved aspect ratio using 384:-1 scaling
- Maintained normalized bounding box coordinates

### WT3 - Model Training
- Trained a pretrained YOLO model on custom dataset
- Used multiple epochs for training
- Monitored training loss and validation loss
- Generated trained weights (best.pt and last.pt)

### WT4 - Object Detection
- Used trained weights on test images
- Detected custom classes from test dataset
- Generated output images with bounding boxes

### WT5 - Final Output Generation
- Combined prediction outputs into video format
- Generated final detection results
- Demonstrated complete end-to-end computer vision workflow

## Classes Used
- Bicycle
- Traffic Signal

## Tools and Technologies
- Python
- Label Studio
- Ultralytics YOLO
- FFmpeg

## Outcome
Successfully completed the complete computer vision pipeline including dataset preparation, annotation, preprocessing, model training, testing and output generation using custom object detection classes.
