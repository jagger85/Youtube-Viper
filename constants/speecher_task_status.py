from enum import Enum

class SpeecherTaskStatus(Enum):
    PENDING = "pending"
    DOWNLOADING = "downloading"
    TRANSCRIBING = "transcribing"
    PROCESSING = "processing"
    FAILED = "failed"
    COMPLETED = "completed"