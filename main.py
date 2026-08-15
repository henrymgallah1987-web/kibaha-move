from fastapi import FastAPI

app = FastAPI(title="KibahaMove API")

@app.get("/")
def home():
    return {
        "message": "Welcome to KibahaMove",
        "status": "The transport API is running"
    }

@app.get("/transport-modes")
def transport_modes():
    return {
        "modes": [
            "Bus",
            "Daladala",
            "Train",
            "Bajaji",
            "Pikipiki",
            "Taxi"
        ]
    }