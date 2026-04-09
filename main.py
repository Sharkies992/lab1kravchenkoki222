from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

@app.get("/")
async def read_index():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"error": "index.html not found"}

@app.get("/api/test")
async def test_endpoint():
    return {
        "status": "ok",
        "message": "Бекенд ЛР3 успішно пройшов тест",
        "lab": 3,
        "student": "Kravchenko"
    }

@app.get("/api/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "processed": True}