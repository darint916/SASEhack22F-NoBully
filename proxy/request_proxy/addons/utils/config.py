import re


class Config:

    def __init__(self) -> None:
        self.domains = []
        self.blockedWords = []

    def load_cfg(self, config: dict):
        if (config.get('domains')):
            self.domains = [re.compile(i) for i in config['domains']]
        if (config.get('blockedWords')):
            self.blockedWords = [re.compile(i) for i in config['blockedWords']]

        
        