from flask import Flask, jsonify, request, jsonify, json, send_file
from api.endpoints import api_blueprint
from werkzeug.exceptions import HTTPException
from core.config import * 
import whisper
import os

uploads_dir = os.path.join(os.getcwd(),'tmp')
os.makedirs(uploads_dir, exist_ok=True)

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/')

model = whisper.load_model(model_size)

app.config['TRANSCRIPTION_MODEL'] = model

if __name__ == "__main__":
    app.run()


