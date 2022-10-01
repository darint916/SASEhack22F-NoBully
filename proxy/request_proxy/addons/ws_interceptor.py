from typing import Dict, List
from mitmproxy import ctx
from mitmproxy import http
from mitmproxy.websocket import WebSocketMessage
from request_proxy.interface import IMitmProxyAddon
from request_proxy.InterceptedMessage import InterceptedMessage

class InterceptorWs(IMitmProxyAddon):

    def __init__(self):
        self._activated = True
        self.config = {'domains': [], 'words': []}

        self.message_intercepted: List[InterceptedMessage] = []

    def websocket_message(self, flow: http.HTTPFlow):
        if (not self._activated):
            return

        # ctx.log.alert(f"A WS Message has been posted. {flow}")
        msg: WebSocketMessage = flow.websocket.messages[-1]
        ctx.log.alert()

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def report(self) -> Dict[str, str]:
        raise NotImplementedError

    def use_config(self, config):
        raise NotImplementedError

    def activate(self, activate: bool):
        self._activated = activate
        
    def is_activated(self) -> bool:
        raise self._activated

    def addon_name(self) -> str:
        raise "Websocket Interceptor"
