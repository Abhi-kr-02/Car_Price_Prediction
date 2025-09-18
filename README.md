## Car Price Predictor UI

Animated Tailwind + GSAP UI that works with either Flask or FastAPI backends.

### Quickstart

1) Install deps (prefer venv):
```bash
pip install -r requirements.txt
```

2) Run Flask:
```bash
python app_flask.py
```
Open `http://127.0.0.1:5000`.

3) Run FastAPI:
```bash
uvicorn app_fastapi:app --reload --host 0.0.0.0 --port 8000
```
Open `http://127.0.0.1:8000`.

The same UI template is shared by both servers. The JS calls `/server-info` to show which framework is running and `/api/predict` for demo predictions.

### Replace demo model
- Update logic in `app_flask.py` and `app_fastapi.py` inside `/api/predict` to call your trained model.
- Adjust payload mapping from the form in `static/js/app.js` if needed.

### Notes
- Tailwind is via CDN; no build step required.
- Animations via GSAP; graceful fallback without JS.


