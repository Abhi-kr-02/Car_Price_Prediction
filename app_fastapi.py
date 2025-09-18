from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def create_app() -> FastAPI:
    app = FastAPI(title="Car Price Predictor UI")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    templates = Jinja2Templates(directory="templates")

    @app.get("/", response_class=HTMLResponse)
    async def index(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    @app.get("/server-info")
    async def server_info():
        return {"framework": "FastAPI", "mode": "demo"}

    @app.post("/api/predict")
    async def predict(payload: dict):
        year = float(payload.get("year", 2018))
        mileage = float(payload.get("mileage", 60000))
        engine = float(payload.get("engine", 1.6))

        base = 5000.0
        year_component = (year - 2000.0) * 400.0
        engine_component = engine * 1200.0
        mileage_component = max(0.0, 150000.0 - mileage) * 0.04
        price = max(1200.0, base + year_component + engine_component + mileage_component)
        return {"price": round(price, 2)}

    return app


app = create_app()


