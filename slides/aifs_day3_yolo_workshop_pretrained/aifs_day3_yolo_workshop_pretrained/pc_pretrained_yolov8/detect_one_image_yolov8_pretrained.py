from ultralytics import YOLO
import cv2
from pathlib import Path

# =========================
# User settings
# =========================
MODEL_PATH = "yolov8n.pt"          # pretrained COCO model, downloaded automatically by Ultralytics
IMAGE_PATH = "classroom_001.jpg"   # image from Raspberry Pi or laptop webcam
OUTPUT_DIR = "yolo_results"
OUTPUT_NAME = "classroom_001_detected.jpg"

CONF_THRESHOLD = 0.25
IMG_SIZE = 640

# =========================
# Create output folder
# =========================
output_dir = Path(OUTPUT_DIR)
output_dir.mkdir(parents=True, exist_ok=True)

# =========================
# Load pretrained YOLO model
# =========================
model = YOLO(MODEL_PATH)

# =========================
# Run detection on one image
# =========================
results = model.predict(
    source=IMAGE_PATH,
    conf=CONF_THRESHOLD,
    imgsz=IMG_SIZE,
    save=False
)

# =========================
# Get first result
# =========================
result = results[0]

# Print detected objects
print("\nDetected objects:")
for box in result.boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    class_name = model.names[cls_id]
    x1, y1, x2, y2 = box.xyxy[0].tolist()
    print(
        f"{class_name}: confidence={conf:.2f}, "
        f"bbox=({x1:.1f}, {y1:.1f}, {x2:.1f}, {y2:.1f})"
    )

# =========================
# Save annotated image
# =========================
annotated_image = result.plot()
output_path = output_dir / OUTPUT_NAME
cv2.imwrite(str(output_path), annotated_image)
print(f"\nSaved detection result to: {output_path}")
