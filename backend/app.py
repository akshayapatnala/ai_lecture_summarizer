from fastapi import FastAPI, UploadFile, File
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
from recorder_processor import transcribe_audio
from summarizer import summarize_text

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "../uploads"

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_audio(file_path)

    summary = summarize_text(transcript)

    return {
        "transcript": transcript,
        "summary": summary
    }
@app.get("/")
def home():
    return {"message": "AI Lecture Analyzer API Running"}