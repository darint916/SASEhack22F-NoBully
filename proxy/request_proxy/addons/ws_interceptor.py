from typing import Dict, List
from mitmproxy import ctx
from mitmproxy import http
from mitmproxy.websocket import WebSocketMessage
from request_proxy.interface.IMitmProxyAddon import IMitmProxyAddon
from request_proxy.InterceptedMessage import InterceptedMessage

class InterceptorWs(IMitmProxyAddon):

    def __init__(self):
        self._activated = True
        self.config = {'domains': [], 'blockedWords': []}
        self.message_intercepted: List[InterceptedMessage] = []

    def websocket_message(self, flow: http.HTTPFlow):
        if (not self._activated):
            return

        # ctx.log.alert(f"A WS Message has been posted. {flow}")
        msg: WebSocketMessage = flow.websocket.messages[-1]
        ctx.log.alert("")

    def report(self) -> Dict[str, str]:
        return {
            'name': self.addon_name(),
            'activated': self.is_activated(),
            'intercepted': [i.to_dict() for i in self.message_intercepted]
        }

    def use_config(self, config):
        if (config.get('domains')):
            self.config['domains'] = config['domains']
        if (config.get('words')):
            self.config['blockedWords'] = config['blockedWords']

    def activate(self, activate: bool):
        self._activated = activate
        
    def is_activated(self) -> bool:
        return self._activated

    def addon_name(self) -> str:
        return "Websocket Interceptor"
