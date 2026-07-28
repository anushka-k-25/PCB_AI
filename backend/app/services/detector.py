from ultralytics import YOLO
from app.recommendations.repair_engine import get_repair_recommendation
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

        repair_info = get_repair_recommendation(class_name)

        detections.append({
            "defect_code": class_name,
            "confidence": round(confidence, 3),
            "bbox": [
                round(x1, 2),
                round(y1, 2),
                round(x2, 2),
                round(y2, 2)
            ],

            "name": repair_info["name"],
            "severity": repair_info["severity"],
            "description": repair_info["description"],
            "possible_causes": repair_info["possible_causes"],
            "repair_recommendation": repair_info["repair_recommendation"],
            "inspection_tips": repair_info["inspection_tips"]
        })

    output_dir = Path(result.save_dir)

    image_files = list(output_dir.glob("*.jpg")) + list(output_dir.glob("*.jpeg")) + list(output_dir.glob("*.png"))

    annotated_image = max(image_files, key=lambda f: f.stat().st_mtime)

    relative_path = annotated_image.relative_to(Path("runs").resolve())

    return {
        "detections": detections,
        "annotated_image": f"/static/{relative_path.as_posix()}"
    }