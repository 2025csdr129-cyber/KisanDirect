from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from app.api.endpoints import router as api_router
from app.database import engine, Base
from pathlib import Path

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Direct Farmer Marketplace & Logistics Engine",
    description="Problem Statement ID26033: Dual Portal + Driver Mode",
    version="2.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
INDEX_FILE = STATIC_DIR / "index.html"
BUYER_FILE = STATIC_DIR / "buyer.html"
DRIVER_FILE = STATIC_DIR / "driver.html"
SW_FILE = STATIC_DIR / "sw.js"
MANIFEST_FILE = STATIC_DIR / "manifest.json"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/sw.js")
def get_service_worker():
    return FileResponse(SW_FILE, media_type="application/javascript", headers={"Service-Worker-Allowed": "/"})

@app.get("/manifest.json")
def get_manifest():
    return FileResponse(MANIFEST_FILE, media_type="application/json")

@app.get("/", response_class=HTMLResponse)
def serve_farmer_app():
    if not INDEX_FILE.exists():
        return HTMLResponse(content="<h3>index.html not found!</h3>", status_code=404)
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/buyer", response_class=HTMLResponse)
def serve_buyer_app():
    if not BUYER_FILE.exists():
        return HTMLResponse(content="<h3>buyer.html not found!</h3>", status_code=404)
    with open(BUYER_FILE, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/driver", response_class=HTMLResponse)
def serve_driver_app():
    if not DRIVER_FILE.exists():
        return HTMLResponse(content="<h3>driver.html not found!</h3>", status_code=404)
    with open(DRIVER_FILE, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
