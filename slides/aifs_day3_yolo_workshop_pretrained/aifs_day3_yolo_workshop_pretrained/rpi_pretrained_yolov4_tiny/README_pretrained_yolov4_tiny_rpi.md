# Pretrained YOLOv4-tiny on Raspberry Pi Zero 2 W

This version does **not** require labeling or training. It uses pretrained YOLOv4-tiny weights trained on COCO classes.

## 1. Install packages

```bash
sudo apt update
sudo apt install -y python3-opencv python3-numpy wget
```

If you use a virtual environment instead:

```bash
pip install -r ../scripts/requirements_rpi_yolov4_tiny.txt
```

## 2. Download pretrained model files

```bash
cd rpi_pretrained_yolov4_tiny
bash download_yolov4_tiny_assets.sh
```

If the Raspberry Pi has no internet, run the same command on a laptop and copy this folder to the Pi.

## 3. Capture an image

```bash
mkdir -p ~/aifs_classroom_yolo/images
rpicam-still -o ~/aifs_classroom_yolo/images/classroom_001.jpg --width 1280 --height 720 --timeout 1000 --nopreview
```

## 4. Detect objects

```bash
python3 detect_yolov4_tiny_rpi.py \
  --image ~/aifs_classroom_yolo/images/classroom_001.jpg \
  --output yolo_results/classroom_001_detected.jpg
```

## Notes

- This is single-image inference, not real-time detection.
- It recognizes common COCO classes such as person, bottle, cup, chair, backpack, book, laptop, and keyboard-like objects depending on the model class list.
- The Raspberry Pi Zero 2 W is slow for deep learning. Use a clear image and be patient.
