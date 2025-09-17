# AI-Powered Smart Glasses for Assistive Technology

This repository contains the source code for an AI-powered smart glasses prototype designed to assist visually impaired individuals. The project uses real-time computer vision and voice feedback to describe the user's surroundings.

This project was developed in two main stages, showcasing an evolution from a basic implementation to a more advanced, high-performance system.

## Project Versions

This repository contains two distinct versions of the application:

### 1. **V1 - TensorFlow Lite Implementation**
-   **Location:** `/v1_tflite_implementation`
-   **Description:** The initial version of the project, built using a pre-trained SSD-MobileNet model on the TensorFlow Lite framework. It provides basic object detection.
-   **Performance:** A functional baseline, suitable for low-power devices but with noticeable latency.

### 2. **V2 - YOLOv8 Implementation**
-   **Location:** `/v2_yolov8_implementation`
-   **Description:** The current, advanced version of the project. It uses the state-of-the-art YOLOv8 model for significantly faster and more accurate object detection.
-   **Core Features:**
    -   Real-time object detection and distance estimation.
    -   Interactive Q&A mode via voice commands ("What do you see?", "How far is the person?").
    -   Facial recognition for known individuals.
    -   Optical Character Recognition (OCR) to read text.
-   **This is the recommended version to run.**

## Setup and Usage
For instructions on how to set up and run each version, please refer to the `README.md` file located inside each respective implementation folder.
```

### **Step 3: Create a Universal `.gitignore` and `requirements.txt`**

In the main `AI-Smart-Glasses` folder, create:
1.  **A `.gitignore` file:** This should contain rules to ignore cache, virtual environments, and large model files (`*.pt`).
2.  **A `requirements.txt` file:** This should list the libraries needed for the more advanced **YOLOv8 version**, as it includes all the dependencies of the TFLite version and more. Run `pip freeze > requirements.txt` from a terminal where you have the V2 dependencies installed.

### **Step 4: Create a New Repository and Upload**

Now, you can upload this organized folder to a fresh GitHub repository using the web interface, which is the most direct method.[1]

1.  **Go to GitHub.com** and click the "**+**" icon in the top-right corner, then select "**New repository**".[2]
2.  **Name your repository** `AI-Smart-Glasses`.
3.  **Do NOT** check the box to add a README, .gitignore, or license. You have already created these.
4.  Click "**Create repository**".[2]
5.  On the new repository page, you will see a "Quick setup" section. Look for the link that says "**uploading an existing file**". Click it.[3]
6.  **Drag and drop** your entire `AI-Smart-Glasses` folder (along with all its contents and sub-folders) onto the page.
7.  Wait for all the files to upload.
8.  Add a commit message like "Initial commit: Add V1 (TFLite) and V2 (YOLOv8) versions".
9.  Click "**Commit changes**".[4]

Your repository is now live with a clean, professional structure that clearly presents both versions of your project in a single `main` branch.
