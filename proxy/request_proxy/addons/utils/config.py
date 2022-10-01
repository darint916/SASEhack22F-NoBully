import re


class Config:

    def __init__(self) -> None:
        self.domains = [re.compile(".*instagram.com.*")]
        self.blockedWords = ["abcd"]

    def load_cfg(self, config: dict):
        # if (config.get('domains')):
        #     self.domains = [re.compile(i) for i in config['domains']]
        # if (config.get('blockedWords')):
        #     # self.blockedWords = [re.compile(i) for i in config['blockedWords']]
        #     self.blockedWords = config['blockedWords']        
        pass