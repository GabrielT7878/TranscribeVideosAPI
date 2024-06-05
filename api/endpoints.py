from flask import request, jsonify, current_app
from api import api_blueprint
from services.video_processing import process_video
from services.transcription import transcribe

@api_blueprint.route('video', methods=['POST'])
def transcribe_video():
    audio_path = process_video(request)
    model = current_app.config['TRANSCRIPTION_MODEL']
    result = transcribe(audio_path,model)
    return jsonify({"text": result["text"]})
