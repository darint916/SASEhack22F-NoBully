import re
from mitmproxy import ctx


class Config:

    def __init__(self) -> None:
        self.domains = []
        self.blockedWords = []

    def load_cfg(self, config: dict):
        ctx.log.error(f"Config received: {config}")
        if (config.get('domain')):
            self.domains = [re.compile(i) for i in config['domain']]
        if (config.get('blockedWords')):
            self.blockedWords = config['blockedWords']
            # self.blockedWords = config['blockedWords']  
            # 

    def __str__(self) -> str:
        return f"Domains: {self.domains}, Blocked words: {self.blockedWords}"      
