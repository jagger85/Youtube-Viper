import os 
import uuid
import tempfile
import shutil

class FileManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
            cls._instance._temp_dir = None
            # Force initialization
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        # Only initialize if it hasn't been initialized yet
        if not hasattr(self, '_initialized'):
            self._temp_dir = None
            self._initialized = True

    @property
    def temp_dir(self) -> str:
        return self._temp_dir

    def create_temp_dir(self):
        self._temp_dir = tempfile.mkdtemp()

    def cleanup_temp_dir(self):
        if self._temp_dir and os.path.exists(self._temp_dir):
            shutil.rmtree(self._temp_dir)
            self._temp_dir = None

    def generate_unique_filename(self, prefix: str, extension: str) -> str:
        if extension:
            return f"{prefix}_{uuid.uuid4().hex}.{extension}"
        return f"{prefix}_{uuid.uuid4().hex}"

    def create_file(self, filename: str) -> str:
        if not self._temp_dir:
            self.create_temp_dir()

        file_path = os.path.join(self._temp_dir, filename)
        open(file_path, 'a').close()
        return file_path

    def delete_file(self, filename: str):
        if not self._temp_dir:
            return

        file_path = os.path.join(self._temp_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)

    