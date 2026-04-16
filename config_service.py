# =========================================
# config_service.py
# Responsible for fetching station config
# from backend API (NOT from AI server logic)
# =========================================

import requests


def get_station_config(station_id: str):
    """
    Fetch configuration for a specific fuel station
    from the backend API.

    This includes:
        - queue_zone (camera ROI area)
        - thresholds (traffic classification rules)

    Args:
        station_id (str): Unique ID of fuel station (e.g., "S1")

    Returns:
        dict: JSON response containing station configuration

    Example response:
        {
            "queue_zone": [100, 200, 800, 600],
            "thresholds": {
                "LOW": 3,
                "MEDIUM": 7
            }
        }

    NOTE:
        This function is part of the SERVICE LAYER.
        It should NOT be placed inside utils.py because it
        performs external network communication.
    """

    # Build backend API URL dynamically using station ID
    url = f"https://api.yourbackend.com/station/{station_id}/config"

    try:
        # Send HTTP GET request to backend
        response = requests.get(url, timeout=5)

        # Raise error if request failed (4xx, 5xx)
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        return response.json()

    except requests.RequestException as e:
        # Handle network or API failure safely
        # In production, you may log this error instead
        return {
            "error": "Failed to fetch station config",
            "details": str(e)
        }