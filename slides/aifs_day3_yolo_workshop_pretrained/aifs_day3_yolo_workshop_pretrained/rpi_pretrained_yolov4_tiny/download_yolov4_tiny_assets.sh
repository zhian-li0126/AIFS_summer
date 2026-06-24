#!/usr/bin/env bash
set -e
mkdir -p models
cd models

# Pretrained YOLOv4-tiny COCO assets. Download on the Pi if it has internet,
# or run this on a laptop and copy the models/ folder to the Pi.
wget -nc https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
wget -nc https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
wget -nc https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

echo "Downloaded models/yolov4-tiny.cfg, models/yolov4-tiny.weights, and models/coco.names"
