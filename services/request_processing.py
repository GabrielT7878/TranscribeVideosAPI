from utils.audio_conversion import extract_audio_from_video
from werkzeug.utils import secure_filename
from config import * 
import os

def process_video(request):
    try:
        uploads_dir = os.path.join(os.getcwd(),tempFolder)
        file = request.files['file']
        file_path = os.path.join(uploads_dir, secure_filename(file.filename))
        file.save(file_path)
        audio_path = extract_audio_from_video(file_path)
        os.remove(file_path)
    except:
         raise Exception("Error while processing the video")
    
    return audio_path

def process_audio(request):
    try:
        uploads_dir = os.path.join(os.getcwd(),tempFolder)
        file = request.files['file']
        audio_path = os.path.join(uploads_dir, secure_filename(file.filename))
        file.save(audio_path)
    except:
         raise Exception("Error while processing the audio")
    return audio_path

