"""
Pretrained YOLOv4-tiny object detection on one Raspberry Pi image.
No labeling or training is needed: this uses COCO pretrained weights.

Example:
python3 detect_yolov4_tiny_rpi.py \
  --image ~/aifs_classroom_yolo/images/classroom_001.jpg \
  --output yolo_results/classroom_001_detected.jpg
"""

import argparse
from pathlib import Path
import cv2
import numpy as np


def load_names(path: Path):
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=True, help='Path to input image')
    parser.add_argument('--output', default='yolo_results/detected.jpg', help='Path to save annotated image')
    parser.add_argument('--cfg', default='models/yolov4-tiny.cfg')
    parser.add_argument('--weights', default='models/yolov4-tiny.weights')
    parser.add_argument('--names', default='models/coco.names')
    parser.add_argument('--conf', type=float, default=0.25)
    parser.add_argument('--nms', type=float, default=0.4)
    parser.add_argument('--size', type=int, default=416)
    args = parser.parse_args()

    image_path = Path(args.image).expanduser()
    output_path = Path(args.output).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cfg = Path(args.cfg)
    weights = Path(args.weights)
    names = Path(args.names)
    if not cfg.exists() or not weights.exists() or not names.exists():
        raise FileNotFoundError('Missing model assets. Run: bash download_yolov4_tiny_assets.sh')

    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f'Could not read image: {image_path}')

    class_names = load_names(names)
    net = cv2.dnn.readNetFromDarknet(str(cfg), str(weights))
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    height, width = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (args.size, args.size), swapRB=True, crop=False)
    net.setInput(blob)

    layer_names = net.getLayerNames()
    out_layer_indices = net.getUnconnectedOutLayers().flatten()
    output_layer_names = [layer_names[i - 1] for i in out_layer_indices]
    outputs = net.forward(output_layer_names)

    boxes, confidences, class_ids = [], [], []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = int(np.argmax(scores))
            confidence = float(scores[class_id])
            if confidence >= args.conf:
                cx, cy, w, h = detection[:4] * np.array([width, height, width, height])
                x = int(cx - w / 2)
                y = int(cy - h / 2)
                boxes.append([x, y, int(w), int(h)])
                confidences.append(confidence)
                class_ids.append(class_id)

    keep = cv2.dnn.NMSBoxes(boxes, confidences, args.conf, args.nms)
    print('\nDetected objects:')
    if len(keep) == 0:
        print('No objects detected. Try a clearer image or lower --conf to 0.15')
    else:
        for i in keep.flatten():
            x, y, w, h = boxes[i]
            label = class_names[class_ids[i]] if class_ids[i] < len(class_names) else str(class_ids[i])
            conf = confidences[i]
            print(f'{label}: confidence={conf:.2f}, bbox=({x}, {y}, {x+w}, {y+h})')
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image, f'{label} {conf:.2f}', (x, max(y - 8, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imwrite(str(output_path), image)
    print(f'\nSaved detection result to: {output_path}')


if __name__ == '__main__':
    main()
