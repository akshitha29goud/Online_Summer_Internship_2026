from ultralytics import YOLO

# Load segmentation model
model = YOLO("yolov8n-seg.pt")

# Run prediction (optional)
model.predict(source="frames", save=True)

# Run training to generate metrics
model.train(data="coco128-seg.yaml", epochs=1)

print("Metrics generated successfully!")