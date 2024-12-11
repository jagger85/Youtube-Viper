import yt_dlp
import logging
import os
from services import FileManager, FileContext


logger = logging.getLogger(__name__)

def download_audio(url: str):
    file_manager = FileManager()
    
    # Ensure temp directory exists
    if not file_manager.temp_dir:
        file_manager.create_temp_dir()
    
    # Generate full paths in temp directory
    temp_filename = file_manager.generate_unique_filename('audio', '')
    temp_filepath = os.path.join(file_manager.temp_dir, temp_filename)
    
    final_filename = file_manager.generate_unique_filename('audio', 'mp3')
    final_filepath = os.path.join(file_manager.temp_dir, final_filename)

    ydl_opts = {
        'format': 'worstaudio/worst',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '64',
        }],
        'outtmpl': temp_filepath,  # yt-dlp will add .mp3 extension
        'nocache': True,
        'verbose': False,
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_filepath = ydl.prepare_filename(info)
            
            # Add .mp3 extension to the downloaded filepath since yt-dlp adds it
            if not downloaded_filepath.endswith('.mp3'):
                downloaded_filepath = f"{downloaded_filepath}.mp3"
            
            with FileContext(downloaded_filepath, 'rb') as source, FileContext(final_filepath, 'wb') as dest:
                dest.write(source.read())

            # Clean up the temporary file
            file_manager.delete_file(os.path.basename(downloaded_filepath))
            
        return final_filepath
    except Exception as e:
        # Clean up both files in case of error
        try:
            if 'downloaded_filepath' in locals():
                file_manager.delete_file(os.path.basename(downloaded_filepath))
            file_manager.delete_file(final_filename)
        except:
            pass
        logger.error(f"An error occurred: {e}")
        raise

