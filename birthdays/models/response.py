from enum import Enum

class Response:
    def __init__(self, status, msg):
        self.status = status
        self.msg = msg

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
    
    def get_msg(self):
        return self.msg
    
    def set_msg(self, msg):
        self.msg = msg

class Status(Enum):
    OK = 'OK'
    FAIL = 'FAIL'
