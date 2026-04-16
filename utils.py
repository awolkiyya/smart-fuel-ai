# =========================================
# utils.py
# Helper functions used across AI system
# =========================================

from typing import Tuple


def is_inside_zone(
    cx: float,
    cy: float,
    zone: Tuple[int, int, int, int]
) -> bool:
    """
    Check if a detected vehicle center point
    is inside the defined QUEUE_ZONE.

    Args:
        cx (float): center X of detected object
        cy (float): center Y of detected object
        zone (tuple): (x1, y1, x2, y2)

    Returns:
        bool: True if inside queue zone, else False
    """
    x1, y1, x2, y2 = zone
    return x1 < cx < x2 and y1 < cy < y2


def get_traffic_status(
    count: int,
    low: int = 3,
    medium: int = 7
) -> str:
    """
    Convert vehicle queue count into traffic level.

    Business logic:
        - LOW    → low congestion
        - MEDIUM → moderate congestion
        - HIGH   → heavy congestion

    Args:
        count (int): number of vehicles in queue zone
        low (int): threshold for LOW status
        medium (int): threshold for MEDIUM status

    Returns:
        str: traffic status
    """

    if count <= low:
        return "LOW"
    elif count <= medium:
        return "MEDIUM"
    else:
        return "HIGH"