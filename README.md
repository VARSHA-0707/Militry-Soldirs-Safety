# Militry-Soldirs-Safety
# 🎥 Soldier Safety Video Player

A simple Python script to load and play a video file using OpenCV. Ideal for reviewing surveillance or training footage in a straightforward, interactive viewer.

---

## 📦 Features

* Play any video file frame-by-frame
* Display the video in a window
* Press `q` to quit the video anytime

---

## 🧰 Requirements

* Python 3.6+
* OpenCV (`opencv-python`)

Install OpenCV using pip:

```bash
pip install opencv-python
```

---

## 📂 Setup and Usage

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/soldier-safety-video.git
cd soldier-safety-video
```

2. **Edit the video path in the script:**

In `main.py`, replace the path with your actual video file location:

```python
video_path = "C:\\Users\\anna_students\\Downloads\\video.png.mp4"
```

3. **Run the script:**

```bash
python main.py
```

4. **Controls:**

* Video will play in a window titled "Soldier Safety Video"
* Press `q` to exit the viewer

---

## 🧾 Code Overview

```python
import cv2

# Load the video file
video_path = "C:\\Users\\anna_students\\Downloads\\video.png.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Loop through each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Soldier Safety Video", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
```
