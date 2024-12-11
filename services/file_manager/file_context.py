"""
File: file_context.py

Purpose:
This file defines the FileContext class, which implements a context manager for safe file handling.
It ensures that files are properly opened and closed, even if exceptions occur during file operations.

Relationship to other files:
- Can be used in conjunction with file_manager.py for safer file operations
- Provides a convenient way to handle files in other parts of the application
"""

class FileContext:
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
