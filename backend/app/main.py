from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.health import router as health_router
from app.core.config import settings
from app.core.logger import logger
from app.api.upload import router as upload_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for PCB Defect Detection and Repair Recommendation System",
    version=settings.VERSION
)


@app.on_event("startup")
async def startup_event():
    logger.info("PCB Defect Detection API Started Successfully")


app.include_router(health_router)
app.include_router(upload_router)
app.mount("/static", StaticFiles(directory="runs"), name="static")

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "Running"
    }