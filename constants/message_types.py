from enum import Enum

class MessageType(Enum):
     LOGIN = "login"
     LOGOUT = "logout"
     OPERATION_STATUS = "operation_status"
     OPERATION_PROGRESS = "operation_progress"
     INFO = "info"
     ERROR = "error"