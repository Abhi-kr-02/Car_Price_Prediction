from __future__ import annotations

from flask import Flask, jsonify, render_template, request
from pathlib import Path


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/server-info")
    def server_info():
        return jsonify({"framework": "Flask", "mode": "demo"})

    @app.post("/api/predict")
    def predict():
        data = request.get_json(force=True, silent=True) or {}
        # Demo heuristic: newer year, larger engine, lower mileage -> higher price
        year = float(data.get("year", 2018))
        mileage = float(data.get("mileage", 60000))
        engine = float(data.get("engine", 1.6))

        base = 5000.0
        year_component = (year - 2000.0) * 400.0
        engine_component = engine * 1200.0
        mileage_component = max(0.0, 150000.0 - mileage) * 0.04
        price = max(1200.0, base + year_component + engine_component + mileage_component)
        return jsonify({"price": round(price, 2)})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


