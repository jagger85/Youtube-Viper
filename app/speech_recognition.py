import whisper
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)

@lru_cache(maxsize=None)
def get_model(model_name = 'base'):
    return whisper.load_model(model_name)


def transcribe_audio(audio_file_path: str):
    model = get_model()

    try:
        # Always translate to English regardless of source language
        result = model.transcribe(
            audio_file_path,
            task="translate",
            fp16=False,
            verbose=True
        )
        return result['text']
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
