import json
from sqlite3 import Timestamp


class InterceptedMessage:

    def __init__(self, message, reason):
        self.request: str = message
        self.response: str = reason
        self.timestamp: str = Timestamp.now()

    def to_dict(self, indent=4):
        return { 
            'request': self.request, 
            'response': self.response,
            'timestamp': self.timestamp
        }
