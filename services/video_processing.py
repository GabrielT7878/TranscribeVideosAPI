from audio_extract import extract_audio
from werkzeug.utils import secure_filename
import os

def process_video(request):
    
    try:
        uploads_dir = os.path.join(os.getcwd(),'tmp')
        file = request.files['file']
        file_path = os.path.join(uploads_dir, secure_filename(file.filename))
        file.save(file_path)
        audio_path = extract_audio_from_video(file_path)
        os.remove(file_path)
    except:
         raise Exception("Error while processing the video")
    
    return audio_path

def extract_audio_from_video(video_path):
        audio_path = video_path.split('.')[0] + '.mp3'

        extract_audio(input_path=video_path, output_path=audio_path)

        return audio_path