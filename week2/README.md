#  Week 02 - Python Virtual Environment & YOLO

---

##  Task 1: Create Virtual Environment

Created a Python virtual environment using venv.

### Command:
python -m venv myenv

---

##  Task 2: Activate Virtual Environment

### Command (Windows):
myenv\Scripts\activate

---

##  Task 3: Install Ultralytics

Installed ultralytics package.

### Command:
pip install -U ultralytics

---

## ✅ Task 4: Object Detection using YOLO

Used pretrained YOLO model for object detection.

### Sample Code:

from ultralytics import YOLO

# Load the latest YOLO26n model (nano version for speed)
model = YOLO("yolo26n.pt")

# Run inference on an image from a URL
results = model("https://ultralytics.com/images/bus.jpg")

# Display the results with bounding boxes
results[0].show()


---

## 📸 Output

(Add your screenshot here)

---

## 🛠 Tools Used

- Python  
- venv  
- Ultralytics YOLO  

---

## 📌 Notes

All tasks executed inside virtual environment.
