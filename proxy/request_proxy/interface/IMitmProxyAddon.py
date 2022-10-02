from typing import Dict


class IMitmProxyAddon:

    def __init__(self) -> None:
        pass

    def report(self) -> Dict[str, str]:
        raise NotImplementedError

    def use_config(self, config):
        raise NotImplementedError

    def activate(self, activate: bool):
        raise NotImplementedError
        
    def is_activated(self) -> bool:
        raise NotImplementedError

    def addon_name(self) -> str:
        raise NotImplementedError
