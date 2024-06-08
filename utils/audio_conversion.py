from audio_extract import extract_audio

def extract_audio_from_video(video_path):
        audio_path = video_path.split('.')[0] + '.mp3'

        extract_audio(input_path=video_path, output_path=audio_path)

        return audio_path