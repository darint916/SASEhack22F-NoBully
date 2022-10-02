import json
from time import time

class InterceptedMessage:

    def __init__(self, message, domain, reason):
        self.message: str = message
        self.domain: str = domain
        self.reason: str = reason
        self.timestamp: str = time()

    def to_dict(self):
        return {
            'message': self.message,
            'domain': self.domain,
            'reason': self.reason,
            'timestamp': self.timestamp
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict())
