from ultralytics import YOLO
import os

# Load segmentation model
model = YOLO("yolov8n-seg.pt")

input_folder = "frames"
output_folder = "seg_output"

os.makedirs(output_folder, exist_ok=True)

for img in os.listdir(input_folder):
    if img.endswith(".jpg"):
        path = os.path.join(input_folder, img)

        results = model.predict(source=path, save=False)

        # Save segmented image
        results[0].save(filename=os.path.join(output_folder, img))

print("Segmentation completed!")