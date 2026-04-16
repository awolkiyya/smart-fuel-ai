# =========================================
# main.py
# AI Server API (FastAPI)
# Entry point for external backend calls
# =========================================

from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
from config_service import get_station_config


from model import detect_queue_count

# Create FastAPI app instance
app = FastAPI()


# -----------------------------------------
# Health check endpoint (server status)
# -----------------------------------------
@app.get("/")
def home():
    return {
        "status": "AI Server Running",
        "service": "YOLO Queue Detection API"
    }


# -----------------------------------------
# MAIN AI ENDPOINT
# -----------------------------------------
@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    station_id: str = "S1"
):
    """
    Endpoint flow:
        1. Receive image from backend/mobile
        2. Convert to OpenCV format
        3. Send to AI model
        4. Return queue analysis result
    """

    # -----------------------------
    # Convert uploaded image to OpenCV format
    # -----------------------------
    contents = await file.read()
    np_img = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    
    # config = get_station_config(station_id)

    # queue_zone = tuple(config["queue_zone"])
    # thresholds = config["thresholds"]

    # -----------------------------
    # Temporary config (later from backend DB)
    # -----------------------------
    queue_zone = (100, 200, 800, 600)
    thresholds = {"LOW": 3, "MEDIUM": 7}

    # -----------------------------
    # Call AI model
    # -----------------------------
    result = detect_queue_count(
        image=image,
        queue_zone=queue_zone,
        station_id=station_id,
        thresholds=thresholds
    )

    return result