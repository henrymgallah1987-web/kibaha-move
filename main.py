from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="KibahaMove API")


routes = [
    {"origin": "Kibaha", "destination": "Maili Moja", "mode": "Bajaji", "fare_tzs": 2000},
    {"origin": "Kibaha", "destination": "Maili Moja", "mode": "Pikipiki", "fare_tzs": 3000},
    {"origin": "Kibaha", "destination": "Maili Moja", "mode": "Taxi", "fare_tzs": 10000},

    {"origin": "Kibaha", "destination": "Mlandizi", "mode": "Daladala", "fare_tzs": 1000},
    {"origin": "Kibaha", "destination": "Mlandizi", "mode": "Bus", "fare_tzs": 1500},

    {"origin": "Kibaha", "destination": "Dar es Salaam", "mode": "Train", "fare_tzs": 2500},
    {"origin": "Kibaha", "destination": "Dar es Salaam", "mode": "Bus", "fare_tzs": 3000},
    {"origin": "Kibaha", "destination": "Dar es Salaam", "mode": "Taxi", "fare_tzs": 45000},
]

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>KibahaMove</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f8fb;
            color: #16324f;
        }

        header {
            background: linear-gradient(120deg, #075985, #0f766e);
            color: white;
            padding: 24px;
        }

        .brand {
            max-width: 900px;
            margin: auto;
        }

        .brand h1 {
            margin: 0;
            font-size: 32px;
        }

        .brand p {
            margin: 8px 0 0;
            color: #d9f5f0;
        }

        main {
            max-width: 900px;
            margin: 35px auto;
            padding: 0 20px;
        }

        .search-card {
            background: white;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 8px 25px rgba(22, 50, 79, 0.12);
        }

        h2 {
            margin-top: 0;
        }

        select, button {
            font-size: 16px;
            padding: 12px;
            border-radius: 8px;
        }

        select {
            border: 1px solid #b7c9d6;
            width: 230px;
        }

        button {
            background: #0f766e;
            color: white;
            border: none;
            margin-left: 8px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background: #115e59;
        }

        #results {
            margin-top: 24px;
            display: grid;
            gap: 14px;
        }

        .route {
            border-left: 6px solid #0f766e;
            background: #ecfdf5;
            padding: 16px;
            border-radius: 8px;
        }

        .fare {
            color: #075985;
            font-size: 20px;
            font-weight: bold;
        }

        .note {
            color: #5b7083;
            font-size: 14px;
            margin-top: 28px;
        }
    </style>
</head>
<body>
    <header>
        <div class="brand">
            <h1>KibahaMove</h1>
            <p>Simple transport route information for Kibaha</p>
        </div>
    </header>

    <main>
        <section class="search-card">
            <h2>Find a route</h2>
            <p>Select your destination to view available sample transport options.</p>

            <select id="destination">
                <option>Maili Moja</option>
                
                <option>Dar es Salaam</option>
            </select>

            <button onclick="searchRoutes()">Find routes</button>

            <div id="results"></div>

            <p class="note">
                Prices are sample estimates and can be updated as real fare information becomes available.
            </p>
        </section>
    </main>

    <script>
        async function searchRoutes() {
            const destination = document.getElementById("destination").value;
            const response = await fetch(
                "/routes/search?origin=Kibaha&destination=" +
                encodeURIComponent(destination)
            );

            const data = await response.json();

            document.getElementById("results").innerHTML =
                data.routes.map(route =>
                    `<div class="route">
                        <strong>${route.mode}</strong><br>
                        From Kibaha to ${destination}<br>
                        <span class="fare">TSh ${route.fare_tzs.toLocaleString()}</span>
                    </div>`
                ).join("") || "<p>No sample route found for this destination.</p>";
        }
    </script>
</body>
</html>
    """


@app.get("/routes/search")
def search_routes(origin: str, destination: str):
    matches = [
        route for route in routes
        if route["origin"].lower() == origin.lower()
        and route["destination"].lower() == destination.lower()
    ]

    return {"routes": matches}