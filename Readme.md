# Fire Segmentation using YOLOv8

## Overview
This project implements fire segmentation using the YOLOv8 model. The model is trained to detect and segment fire in CCTV footage videos or any Videos, making it useful for applications in fire detection and safety monitoring.

## Results

### Image Output:
![Fire Segmentation Output](https://github.com/user-attachments/assets/d9e71ae3-25dd-469d-ad91-61fd538f47ad)

### Video Output:
[Watch the video](https://github.com/user-attachments/assets/8932873d-f58f-4448-a360-6c1c6725d2e7)

## Installation

To get started, clone this repository and install the required packages:
```bash
git clone https://github.com/yourusername/fire-segmentation.git
cd fire-segmentation
# Please install below requirements
Requirements
Python 3.10 
PyTorch
Ultralytics YOLOv8
Roboflow
```
You can install the necessary packages using:

pip install ultralytics==8.0.196 roboflow

Usage
To run the fire segmentation model, use the following command:

from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# Predict on a video source (0 for webcam)
model.predict(source=0, show=True, save=True, hide_labels=True, hide_conf=True, conf=0.5, save_txt=False, save_crop=False, line_thickness=2, boxes=False)

# Dataset
The dataset used for training the model is annotated on Roboflow. And then that anotated dataset is imported on the Google colab notebook for training.

# Training
Model training of the YoloV8 is done on the google Colab notebook which is shared in this repository. For training annotated dataset is imported from Roboflow and the model is trained on 100 epochs.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

