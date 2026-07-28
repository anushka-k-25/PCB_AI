from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    return {
        "status": "Healthy",
        "message": "PCB Defect Detection API is running successfully."
    }