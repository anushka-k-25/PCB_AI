from ultralytics import YOLO


def main():
    model = YOLO("yolo11n.pt")

    model.train(
        data="../dataset/raw/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        device=0,
        workers=0,   # Important for Windows
        project="./training/runs",
        name="pcb_defect_detection"
    )


if __name__ == "__main__":
    main()