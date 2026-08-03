from ultralytics import YOLO


def main():
    model = YOLO("yolo11n.pt")

    model.train(
        data="../dataset/raw/data.yaml", # address of the dataset file
        epochs=100,
        imgsz=640,
        batch=16, # leatn in batches of 16 images
        device=0,
        workers=0,   # Important for Windows
        project="./training/runs",
        name="pcb_defect_detection"
    )


if __name__ == "__main__":
    main()