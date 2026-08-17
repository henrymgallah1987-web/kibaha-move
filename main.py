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
        "modes": ["Bus", "Daladala", "Train", "Bajaji", "Pikipiki", "Taxi"]
    }


@app.get("/routes/search")
def search_routes(origin: str, destination: str):
    return {
        "origin": origin,
        "destination": destination,
        "results_found": 2,
        "routes": [
            {"mode": "Bajaji", "fare_tzs": 2000},
            {"mode": "Pikipiki", "fare_tzs": 3000}
        ]
    }
