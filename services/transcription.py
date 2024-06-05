import whisper

def transcribe(audio_path,model):
    result = model.transcribe(audio_path)
    return result