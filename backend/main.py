from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "EduProof API Running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    
    with open("temp.png", "wb") as f:
        f.write(content)

    text = pytesseract.image_to_string(Image.open("temp.png"))

    return {"extracted_text": text}
