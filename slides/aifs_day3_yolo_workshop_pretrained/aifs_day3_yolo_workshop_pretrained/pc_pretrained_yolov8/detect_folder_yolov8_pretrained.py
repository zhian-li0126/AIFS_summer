from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = "yolov8n.pt"
IMAGE_FOLDER = "rpi_classroom_images"
OUTPUT_PROJECT = "yolo_results"
CONF_THRESHOLD = 0.25
IMG_SIZE = 640

model = YOLO(MODEL_PATH)
results = model.predict(
    source=IMAGE_FOLDER,
    conf=CONF_THRESHOLD,
    imgsz=IMG_SIZE,
    save=True,
    project=OUTPUT_PROJECT,
    name="classroom_folder_detected",
    exist_ok=True
)

print(f"Processed {len(results)} image(s).")
print(f"Saved annotated images under: {Path(OUTPUT_PROJECT) / 'classroom_folder_detected'}")
