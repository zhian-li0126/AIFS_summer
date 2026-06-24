# AIFS Day 3 YOLO Workshop: Pretrained Classroom Object Detection

This package is designed for a short Raspberry Pi + camera workshop.

Main idea: students capture classroom images and run a **pretrained YOLO detector**. No labeling or custom training is required.

## Recommended sequence

1. Raspberry Pi: test camera with `rpicam-hello`.
2. Raspberry Pi: capture one or more classroom object images with `rpicam-still`.
3. Raspberry Pi local version: run pretrained YOLOv4-tiny using OpenCV DNN.
4. PC / Colab version: run pretrained YOLOv8n with Ultralytics.
5. Optional extension: explore Kaggle datasets and think about custom training later.
