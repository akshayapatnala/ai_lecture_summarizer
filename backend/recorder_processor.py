import whisper
import subprocess

model = whisper.load_model("base")

def transcribe_audio(video_path):

    audio_path = video_path + ".wav"

    # convert video to audio
    subprocess.run([
        "ffmpeg",
        "-i", video_path,
        "-ar", "16000",
        "-ac", "1",
        audio_path
    ])

    result = model.transcribe(audio_path)

    return result["text"]