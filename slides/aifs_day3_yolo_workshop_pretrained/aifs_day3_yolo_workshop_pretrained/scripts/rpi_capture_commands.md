# Raspberry Pi Zero 2 W Camera Commands

Use these commands on Raspberry Pi OS with the new Raspberry Pi camera stack.

```bash
# 1) Preview the camera for 5 seconds
rpicam-hello -t 5000

# 2) Make a folder for workshop images
mkdir -p ~/aifs_classroom_yolo/images

# 3) Capture one image
rpicam-still -o ~/aifs_classroom_yolo/images/classroom_001.jpg \
  --width 1280 --height 720 --timeout 1000 --nopreview

# 4) Capture 20 images with automatic names
for i in $(seq -w 1 20); do
  rpicam-still -o ~/aifs_classroom_yolo/images/classroom_${i}.jpg \
    --width 1280 --height 720 --timeout 1000 --nopreview
  sleep 2
done
```

Legacy fallback on older Raspberry Pi OS images:

```bash
libcamera-hello -t 5000
libcamera-still -o ~/aifs_classroom_yolo/images/classroom_001.jpg --width 1280 --height 720 -t 1000 --nopreview
```
