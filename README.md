# AI-Powered PCB Defect Detection and Repair Recommendation System

An end-to-end AI-powered web application for detecting Printed Circuit Board (PCB) defects using **YOLO11**, providing **repair recommendations**, and generating inspection reports through a modern web interface.

---

## Project Overview

This project uses a custom-trained YOLO11 object detection model to automatically identify defects in PCB images. Users can upload an image through a web application, receive detected defects with confidence scores, and view recommended repair actions.

The system is designed to reduce manual inspection time and improve PCB quality assurance by leveraging deep learning and computer vision.

---

## Features

- PCB defect detection using a custom YOLO11 model
- Upload PCB images for analysis
- Bounding box visualization with confidence scores
- Repair recommendation for each detected defect
- FastAPI backend for inference
- DeepPCB dataset-based model training
- PDF inspection report generation
- React-based responsive frontend

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Deep Learning | YOLO11 (Ultralytics) |
| Framework | PyTorch |
| Image Processing | OpenCV |
| Frontend | React + Vite |
| Language | Python |
| Version Control | Git & GitHub |
---

## Project Structure

```text
PCB_AI/
│
├── backend/
│   ├── app/
│   ├── uploads/
│   ├── runs/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── screenshots/
├── training/
├── README.md
└── .gitignore
```
---

## Model Performance

The object detection model was trained on the **DeepPCB** dataset using **YOLO11**.

### Detection Capabilities

- Missing Hole
- Mouse Bite
- Open Circuit
- Short Circuit
- Spur
- Spurious Copper

The trained model is integrated into the FastAPI backend for real-time inference.

---

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PCB_AI.git
cd PCB_AI
```

---

### 2. Create and Activate a Virtual Environment

#### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

### 4. Run the Backend Server

```bash
uvicorn app.main:app --reload
```

The backend will start at:

```
http://127.0.0.1:8000
```

---

### 5. Open a New Terminal

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the React application:

```bash
npm run dev
```

The frontend will start at:

```
http://localhost:5173
```

---

### 6. Open the Application

Visit:

```
http://localhost:5173
```

Upload a PCB image and start detecting defects.

---
## Screenshots

### Swagger API

![Swagger API](screenshots/swagger.png)

### Detection Result

![Detection Result](screenshots/detection_result.png)

### API Response

![API Response](screenshots/api_response.png)

### Training Results

![Training Results](screenshots/training_results.png)

### Confusion Matrix

![Confusion Matrix](screenshots/confusion_matrix.png)

---

## 🎥 Demo Video

Click the video below to watch the project demonstration.

[▶️ Demo Video](screenshots/demo-video.mp4)

## Future Enhancements

- User authentication
- Detection history dashboard
- Live camera inspection
- Batch image processing
- Cloud deployment
- Multi-class PCB defect analytics

## License

This project is intended for educational and research purposes.