from pathlib import Path
import shutil #used to copy the uploaded file to the uploads directory

from fastapi import APIRouter, File, HTTPException, UploadFile
#These are FastAPI classes.
#UploadFile : Represents the uploaded image.
#File : Used to specify that the uploaded file is expected to be of type File.
#HTTPException : Used to raise an HTTP exception if the uploaded file is not of the allowed types.

from app.services.detector import detect #This imports the detect function from the detector.py file. The detect function is responsible for running the YOLOv8 model on the uploaded image and returning the detection results.

router = APIRouter( #Creates an API route.
    prefix="/upload",
    tags=["Upload"]
)
#creating a directory named "uploads" to store the uploaded images. If the directory already exists, it will not raise an error due to exist_ok=True.
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/") #Defines a POST endpoint for the "/upload" route. Execute the function below 
async def upload_image(file: UploadFile = File(...)): #the function takes an uploaded file as input. The file parameter is of type UploadFile, which represents the uploaded image. The File(...) indicates that the file is expected to be of type File.
    allowed_extensions = {".jpg", ".jpeg", ".png"}

    extension = Path(file.filename).suffix.lower() #Extracts the file extension from the uploaded file's filename and converts it to lowercase. This is done to ensure that the extension check is case-insensitive.

    if extension not in allowed_extensions: #other than the allowed extensions, it raises an HTTPException with a status code of 400 (Bad Request) and a message indicating that only JPG, JPEG, and PNG images are allowed.
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG images are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = detect(str(file_path)) #calls the detect function from the detector.py file, passing the path of the uploaded image as an argument. The detect function runs the YOLOv8 model on the image and returns the detection results.

    return {
    "success": True,
    "message": "Detection completed successfully.",
    "filename": file.filename,
    "total_detections": len(results["detections"]),
    "detections": results["detections"],
    "annotated_image": results["annotated_image"]
}

"""
Image Upload API

This file implements the image upload API using FastAPI.

Workflow:
1. Receives the uploaded PCB image from the React frontend.
2. Validates that the uploaded file is in JPG, JPEG, or PNG format.
3. Saves the image in the 'uploads' directory.
4. Calls the detect() function from detector.py to perform PCB defect detection using the trained YOLO11 model.
5. Receives the detection results, including defect details and the annotated image.
6. Returns a JSON response containing:
   - Upload status
   - Success message
   - Uploaded filename
   - Total number of detected defects
   - Detection details
   - Annotated image path

The React frontend uses this response to display the detected PCB image,
defect information, repair recommendations, and summary statistics.
"""