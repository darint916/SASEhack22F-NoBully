import re
from typing import Dict, List
from flask import Config
from mitmproxy import ctx
from mitmproxy import http
from mitmproxy.websocket import WebSocketMessage
from request_proxy.addons.utils.config import Config
from request_proxy.interface.IMitmProxyAddon import IMitmProxyAddon
from request_proxy.InterceptedMessage import InterceptedMessage

from request_proxy.addons.utils import utils

class InterceptorHttp(IMitmProxyAddon):

    def __init__(self):
        self._activated = True
        self.config: Config = Config()
        self.message_intercepted: List[InterceptedMessage] = []

    def request(self, flow: http.HTTPFlow) -> None:
        if (not self._activated):
            return

        if (utils.match_url(self.config.domains, flow.request.url)):
            ctx.log.alert(f"Request intercepted. {flow.request.url}")
            self.message_intercepted.append(InterceptedMessage(flow.request.content, flow.request.url, "ASdf"))

    def report(self) -> Dict[str, str]:
        return {
            'name': self.addon_name(),
            'activated': self.is_activated(),
            'intercepted': [i.to_dict() for i in self.message_intercepted]
        }

    def use_config(self, config):
        ctx.log.info(f"Config received: {config}")
        self.config.load_cfg(config)

    def activate(self, activate: bool):
        self._activated = activate
        
    def is_activated(self) -> bool:
        return self._activated

    def addon_name(self) -> str:
        return "Http Interceptor"
