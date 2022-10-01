import json
from sqlite3 import Timestamp


class InterceptedMessage:

    def __init__(self, message, domain, reason):
        self.message: str = message
        self.domain: str = domain
        self.reason: str = reason
        self.timestamp: str = Timestamp.now()

    def to_dict(self, indent=4):
        return {
            'message': self.message,
            'domain': self.domain,
            'reason': self.reason,
            'timestamp': self.timestamp
        }
