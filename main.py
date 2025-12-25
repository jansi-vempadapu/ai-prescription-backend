from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    text = pytesseract.image_to_string(image)
    return {"text": text}
