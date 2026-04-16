Here is a **clean, professional, “investor-ready” README.md** for your AI server project. You can copy-paste it directly into GitHub.

---

```markdown
# 🚀 Smart Fuel Station AI Queue Monitoring System

## 🧠 AI Server (YOLO + FastAPI)

This project is an AI-powered microservice that detects vehicles in fuel station camera feeds and estimates real-time queue length and traffic congestion levels.

It is designed for **smart city fuel station optimization and traffic intelligence systems**.

---

# 📸 Demo Screenshots

Below are real outputs from the AI system running YOLO-based vehicle detection:

---

## 🚗 Fuel Station Vehicle Detection
<img src="https://raw.githubusercontent.com/awolkiyya/smart-fuel-ai/main/screenshots/demo1.png" width="700"/>

---

## 📊 Queue Analysis API Response
<img src="https://raw.githubusercontent.com/awolkiyya/smart-fuel-ai/main/screenshots/demo2.png" width="700"/>

---

## 🚦 Traffic Status Classification
<img src="./screenshots/demo3.png" width="700"/>

# 📌 System Overview

The AI server receives images from a backend system (or CCTV/mobile camera), runs object detection using YOLO, and returns:

- 🚗 Vehicle count in queue area
- 📊 Traffic congestion status (LOW / MEDIUM / HIGH)
- 📍 Station-based analytics support

---

# 🏗️ Architecture

```

Mobile / CCTV Camera
↓
Backend API (Node.js / Laravel)
↓
AI Server (FastAPI + YOLO)
↓
AI Processing Engine
↓
JSON Response (Queue + Traffic Status)

````

---

# 🤖 AI Technology Stack

- :contentReference[oaicite:0]{index=0} (Vehicle detection)
- :contentReference[oaicite:1]{index=1} (AI API service)
- OpenCV (Image processing)
- NumPy (Array processing)

---

# 🚗 Detected Vehicle Classes

The system focuses on real fuel station traffic:

```python
car
truck
bus
motorcycle
```

❌ Excluded:
- persons
- bicycles
- animals
- non-vehicle objects

---

# ⚙️ Core Features

## ✔ Vehicle Detection
Detects vehicles from images using YOLO model.

## ✔ Queue Zone Filtering
Only counts vehicles inside a defined region of interest (ROI).

## ✔ Traffic Status Classification

| Vehicle Count | Status |
|--------------|--------|
| 0 - 3        | LOW    |
| 4 - 7        | MEDIUM |
| 8+           | HIGH   |

## ✔ Station-Based Configuration
Each fuel station can have:
- custom queue zone
- custom thresholds
- independent analytics

---

# 📡 API Endpoint

## ▶ POST `/analyze`

### Request (form-data):

| Key        | Type | Description |
|------------|------|-------------|
| file       | File | Image from camera |
| station_id | Text | Station identifier |

---

### Response:

```json
{
  "station_id": "S1",
  "queue_count": 6,
  "traffic_status": "MEDIUM"
}
````

---

# 🚀 How It Works

1. Image is sent from backend or camera
2. AI server receives image
3. YOLO detects vehicles
4. System filters vehicles inside queue zone
5. Counts valid vehicles
6. Applies traffic rules
7. Returns structured JSON response

---

# 🧠 Business Use Case

This system can be used for:

* ⛽ Fuel station queue optimization
* 🚗 Real-time traffic monitoring
* 📊 Smart city analytics
* 📍 Station performance tracking
* 🧭 Driver decision support (choose less crowded stations)

---

# 📦 Project Structure

```

ai-server/
│
├── main.py              # FastAPI entry point
├── model.py            # YOLO detection logic
├── utils.py            # Helper functions
├── config\_service.py   # Backend config fetching
├── requirements.txt    # Dependencies

```

---

# ⚡ Installation

```bash
pip install -r requirements.txt
```

---

# ▶ Run Locally

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🌍 Deployment

Recommended deployment:

* Render (MVP / testing)
* AWS EC2 (production)
* Docker (scalable systems)

---

# 🔐 Configuration System

Each station configuration is managed from backend:

* queue_zone (camera ROI)
* thresholds (traffic rules)

Example:

```json
{
  "queue_zone": [100, 200, 800, 600],
  "thresholds": {
    "LOW": 3,
    "MEDIUM": 7
  }
}
```

---

# 🧠 Future Improvements

* 🎥 Real-time video stream processing (CCTV)
* 📡 WebSocket live updates
* 🧭 Multi-camera fusion system
* 📊 Predictive queue forecasting
* 🧠 Custom trained YOLO model for local vehicles (e.g., Bajaj detection)

---

# 👨‍💻 Developer

Developed by:

**Software Engineer Awol Abdulbaasit**

---

# 🚀 Goal

To build a **smart fuel station intelligence system** that reduces waiting time, improves traffic flow, and enables data-driven station management.

---

# 📌 Summary

This AI server is the **brain of a smart fuel station ecosystem**, providing real-time vehicle queue analysis using computer vision and deep learning.

```

---

If you want next, I can also give you:

- 🚀 :contentReference[oaicite:2]{index=2}
- 📡 :contentReference[oaicite:3]{index=3}
- 📱 :contentReference[oaicite:4]{index=4}
- 🧠 :contentReference[oaicite:5]{index=5}

Just tell me 👍
```
