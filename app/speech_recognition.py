import whisper
from functools import lru_cache

@lru_cache(maxsize=None)
def get_model(model_name = 'base'):
    return whisper.load_model(model_name)


def transcribe_audio(audio_file_path: str):
    model = get_model()

    try:
        result = model.transcribe(audio_file_path)
        return result['text']
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
