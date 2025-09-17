# AI Smart Glasses Project

A computer vision and AI-powered smart glasses system to assist visually impaired users by providing real-time environmental context, object detection, voice feedback, and face/person recognition. This repository contains both TensorFlow Lite and YOLOv8 object detection pipelines, scripts for different use-cases, and setup documentation for various environments including Raspberry Pi.

---

## Features

- **Real-Time Object Detection:** Supports detection via both TensorFlow Lite (efficient for edge devices) and Ultralytics YOLOv8 (for advanced/fast detection).
- **Multiple Input Modes:** Scripts to work with images, video files, and live webcam/camera input.
- **Voice Feedback & Interaction:** Designed to give audio feedback for each detected object/person and answer questions via basic voice commands.
- **Distance Estimation:** Basic distance estimation for recognized objects.
- **Face Recognition:** (For YOLOv8 advanced versions) Extendable to identify known people using face datasets.
- **Cross-Platform:** Can be deployed and tested on PC or configured for Raspberry Pi.

---

## Directory & Important Files

- `coco_ssd_mobilenet_v1_1.0_quant_2018_06_29/` – Pre-trained TFLite model files and label map for legacy detection (TensorFlow Lite).
- `doc/` – System/project-related documentation.
- `tflite1-env/` – Example of Python virtual environment (not needed in repo, recommended to `.gitignore`).
- `README.md` – This project overview.
- `Raspberry_Pi_Guide.md` – Instructions/setup for Raspberry Pi deployment.
- `Result Video 1.mp4`, `Video 2.mp4` – Test/demo videos.
- **TF Lite Scripts:**
    - `TFLite_detection_image.py` – Run object detection on an image.
    - `TFLite_detection_video.py` – Run detection on a video file.
    - `TFLite_detection_webcam.py` – Run detection live via a webcam/camera.
- **YOLOv8 Script:**
    - `YOLOV8_ADVANCED.py` – Advanced detection and assistive features using Ultralytics YOLOv8.
- `auto.py` – [Clarify function or remove if sample/test only.]
- `get_pi_requirements.sh` – Bash script to install dependencies for Pi deployment.
- `overview` – [Clarify/useful or remove if not needed.]
- `test1.jpg`, `yolov8n.pt` – Example image and YOLOv8 model weights.

---

## Setup

1. **Clone this repository:**
    ```
    git clone https://github.com/lakshya051/AISMARTGLASSES.git
    cd AISMARTGLASSES
    ```

2. **(Optional) Set up a Python virtual environment:**
    ```
    python -m venv smartglasses-env
    source smartglasses-env/bin/activate   # On Windows: smartglasses-env\\Scripts\\activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    # For face recognition & YOLOv8 you may also need:
    pip install face_recognition ultralytics
    # For TFLite:
    pip install tflite-runtime pillow numpy opencv-python
    ```

4. **Download/prep the models:**  
   TensorFlow Lite models are provided in `coco_ssd_mobilenet_v1_1.0_quant_2018_06_29/`.  
   Download `yolov8n.pt` from [Ultralytics](https://github.com/ultralytics/ultralytics) or use the one provided.

---

## Usage

### **TensorFlow Lite:**
- On Image:  
    `python TFLite_detection_image.py`
- On Video:  
    `python TFLite_detection_video.py`
- On Webcam:  
    `python TFLite_detection_webcam.py`

### **YOLOv8 (Recommended):**
- Advanced real-time detection & voice feedback, run:  
    `python YOLOV8_ADVANCED.py`

_Refer to in-file comments for further usage details and customization._

---

## Raspberry Pi

See `Raspberry_Pi_Guide.md` for step-by-step hardware setup and system configuration.

---

## Demo

Demo/test videos provided: `Result Video 1.mp4`, `Video 2.mp4`

---

## Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

MIT License

---

**If you like this project, please star ⭐ the repo!**

