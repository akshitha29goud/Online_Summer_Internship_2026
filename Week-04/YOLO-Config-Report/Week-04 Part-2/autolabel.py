from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

# COCO → YOUR CLASS mapping
class_map = {
    0: 0,   # person
    1: 1,   # bicycle
    2: 2,   # car
    9: 3,   # traffic light
    26: 4   # handbag
}

def label_images(image_folder, label_folder):
    os.makedirs(label_folder, exist_ok=True)

    for img in os.listdir(image_folder):
        path = os.path.join(image_folder, img)
        results = model(path)

        for r in results:
            boxes = r.boxes.xywhn
            classes = r.boxes.cls

            label_path = os.path.join(label_folder, img.replace(".jpg", ".txt"))

            with open(label_path, "w") as f:
                for box, cls in zip(boxes, classes):
                    cls = int(cls)

                    if cls in class_map:
                        new_cls = class_map[cls]
                        f.write(f"{new_cls} {' '.join(map(str, box.tolist()))}\n")

print("Auto labeling done!")

label_images("dataset/images/train", "dataset/labels/train")
label_images("dataset/images/val", "dataset/labels/val")