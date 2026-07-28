from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.detector import detect

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def upload_image(file: UploadFile = File(...)):
    allowed_extensions = {".jpg", ".jpeg", ".png"}

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG images are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = detect(str(file_path))

    return {
    "success": True,
    "message": "Detection completed successfully.",
    "filename": file.filename,
    "total_detections": len(results["detections"]),
    "detections": results["detections"],
    "annotated_image": results["annotated_image"]
}