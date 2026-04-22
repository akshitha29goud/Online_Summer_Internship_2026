#  Week 04 
Task 1 - YOLO Dataset Configuration Analysis

---

##  Introduction

YOLO (You Only Look Once) is a real-time object detection model that relies on configuration (meta) files to define dataset structure, class labels, and training parameters. These files play a crucial role in training and evaluating object detection models.

---

##  YAML Configuration File

The dataset configuration file (`coco128.yaml`) defines important information about the dataset.

### Example:

path: ../datasets/coco128  
train: images/train2017  
val: images/train2017  

names:  
0: person  
1: bicycle  
2: car  

---

###  Key Components

- **path** → root directory of dataset  
- **train** → training images folder  
- **val** → validation images folder  
- **names** → class labels with index  

---

##  Dataset Structure

A YOLO dataset follows this structure:

dataset/  
├── images/  
│   ├── train/  
│   └── val/  
├── labels/  
│   ├── train/  
│   └── val/  

Each image has a corresponding label file with the same name.

---

##  Label File Format

Each label file is stored as a `.txt` file with the format:

<class> <x_center> <y_center> <width> <height>

### Example:
0 0.5 0.5 0.2 0.3  

---

###  Explanation

- Class ID corresponds to object type  
- Coordinates are normalized between 0 and 1  
- Represents bounding box position and size  

---

##  Practical Observation

- Located `coco128.yaml` inside ultralytics package (`cfg/datasets/`)
- Observed dataset paths and class definitions
- Explored `images/train` and `labels/train` folders
- Verified that each image has a corresponding label file
- Observed normalized coordinate format in label files
- Confirmed how YOLO uses these files during detection

---

##  Key Insights

- YAML file defines dataset structure and classes  
- Labels store object annotations  
- Proper structure is required for training  
- YOLO relies on normalized coordinates  

---

##  Conclusion

YOLO configuration files are essential for defining how datasets are structured and interpreted. Understanding these files helps in training custom models and improving detection performance.

---



##  References

- Ultralytics YOLO Documentation: https://docs.ultralytics.com  
- YOLO Dataset Format Guide: https://docs.ultralytics.com/datasets/detect/  
- Image Segmentation (Ultralytics): https://docs.ultralytics.com/tasks/segment/  
- Python Virtual Environment (venv): https://docs.python.org/3/library/venv.html  
- YAML File Documentation: https://yaml.org/spec/  
