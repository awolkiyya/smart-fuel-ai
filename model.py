# =========================================
# model.py
# AI inference engine using YOLOv8
# Responsible for vehicle detection
# =========================================

from typing import Dict, Tuple, Optional
from ultralytics import YOLO
from utils import is_inside_zone, get_traffic_status


# -------------------------------------------------
# Load YOLO model ONCE (important for performance)
# -------------------------------------------------
model = YOLO("yolov8n.pt")

# Vehicle classes we care about in fuel station
VEHICLE_CLASSES = {"car", "truck", "bus", "motorcycle"}


def detect_queue_count(
    image,
    queue_zone: Tuple[int, int, int, int],
    station_id: str = "S1",
    thresholds: Optional[Dict[str, int]] = None
) -> Dict:
    """
    Main AI function:
    Detects vehicles in image and calculates queue size.

    Pipeline:
        1. Run YOLO object detection
        2. Filter vehicle classes
        3. Check if vehicle is inside queue zone
        4. Count valid vehicles
        5. Convert count → traffic status

    Args:
        image: input frame (OpenCV image)
        queue_zone: area where queue exists (x1,y1,x2,y2)
        station_id: fuel station identifier
        thresholds: traffic rule configuration

    Returns:
        dict: queue_count + traffic_status
    """

    # Default thresholds if backend does not send config
    if thresholds is None:
        thresholds = {"LOW": 3, "MEDIUM": 7}

    # -----------------------------
    # Run YOLO inference
    # -----------------------------
    results = model(image)[0]

    count = 0

    # -----------------------------
    # Process detection results
    # -----------------------------
    for box in results.boxes:

        # Get detected class index
        cls = int(box.cls[0])

        # Convert index → label (car, truck, etc.)
        label = model.names[cls]

        # Only process vehicles
        if label in VEHICLE_CLASSES:

            # Bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]

            # Calculate center point of vehicle
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2

            # Check if vehicle is inside queue zone
            if is_inside_zone(cx, cy, queue_zone):
                count += 1

    # -----------------------------
    # Convert count → traffic status
    # -----------------------------
    status = get_traffic_status(
        count,
        thresholds["LOW"],
        thresholds["MEDIUM"]
    )

    # -----------------------------
    # Final response object
    # -----------------------------
    return {
        "station_id": station_id,
        "queue_count": count,
        "traffic_status": status
    }