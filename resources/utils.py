"""
This module contains all necessary helper functions for views.py
"""
from datetime import datetime
from uuid import uuid4
import whisper


def generate_unique_filename():
    """
    Generate a unique filename based on the current timestamp and a random unique ID.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid4().hex[:6])
    filename = f"{timestamp}_{unique_id}"
    return filename


def get_file_extension(content_type):
    """
    Get the file extension corresponding to a given content type.
    """
    content_type_map = {
        "video/mp4": "mp4",
        "video/mov": "mov",
        "video/webm": "webm",
    }
    return content_type_map.get(content_type)


def transcribe_audio(audio_path):
    """
    Transcribe audio to text from a given audio file using the Whisper ASR model.
    """
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return str(e)
