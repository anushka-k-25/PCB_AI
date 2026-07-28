from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "best.pt"

model = None


def load_model():
    global model

    if model is None:
        model = YOLO(str(MODEL_PATH))

    return model


def detect(image_path):
    model = load_model()

    results = model.predict(
        source=image_path,
        save=True,
        conf=0.5
    )

    detections = []

    result = results[0]

    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        confidence = float(box.conf[0])

        x1, y1, x2, y2 = map(float, box.xyxy[0])

        detections.append({
            "class": class_name,
            "confidence": round(confidence, 3),
            "bbox": [
                round(x1, 2),
                round(y1, 2),
                round(x2, 2),
                round(y2, 2)
            ]
        })

    return detections