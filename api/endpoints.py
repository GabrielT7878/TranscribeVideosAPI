from flask import request, jsonify, json,current_app, send_file
from functools import wraps
from api import api_blueprint
from services.request_processing import *
from services.transcription import transcribe
from whisper.utils import get_writer
from werkzeug.exceptions import HTTPException
from config import tempFolder
import os

@api_blueprint.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
    })
    response.content_type = "application/json"
    return response


@api_blueprint.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e.name)), 404

def inject_model(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        model = current_app.config['TRANSCRIPTION_MODEL']
        return func(model, *args, **kwargs)
    return wrapper


@api_blueprint.route('/video', methods=['POST'])
@inject_model
def transcribe_video(model):
    audio_path = process_video(request)
    result = transcribe(audio_path,model)
    os.remove(audio_path)
    return jsonify({"text": result["text"]})

@api_blueprint.route('/audio', methods=['POST'])
@inject_model
def transcribe_audio(model):
    audio_path = process_audio(request)
    result = transcribe(audio_path,model)
    os.remove(audio_path)
    return jsonify({"text": result["text"]})

@api_blueprint.route('/srt', methods=['POST'])
@inject_model
def get_srt(model):
    audio_path = process_video(request)
    result = transcribe(audio_path,model)
    os.remove(audio_path)
    writer = get_writer("srt", tempFolder)
    writer(result, audio_path, {})
    index = audio_path.rindex('/')
    srt_file_path =  tempFolder + '/' + audio_path[index+1:len(audio_path)].split('.')[0] + '.srt'
    return send_file(srt_file_path, as_attachment=True)