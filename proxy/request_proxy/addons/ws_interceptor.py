from typing import Dict, List
from mitmproxy import ctx
from mitmproxy import http
from mitmproxy.websocket import WebSocketMessage
from request_proxy.addons.utils import utils
from request_proxy.addons.utils.config import Config
from request_proxy.interface.IMitmProxyAddon import IMitmProxyAddon
from request_proxy.InterceptedMessage import InterceptedMessage

class InterceptorWs(IMitmProxyAddon):

    def __init__(self):
        self._activated = True
        self.config: Config = Config()
        self.message_intercepted: List[InterceptedMessage] = []

    def websocket_message(self, flow: http.HTTPFlow):
        if (not self._activated):
            return

        if (utils.match_url(self.config.domains, flow.request.url)):
            msg = flow.websocket.messages[-1].content
            try:
                msg_idx = msg.index(b'[')
            except ValueError:
                return

            msg_decoded = msg[msg_idx:].decode('utf-8')
            # ctx.log.alert()
            if (utils.match_word(self.config.blockedWords, msg_decoded)):
                ctx.log.alert(f"Websocket message intercepted --. {flow.request.url}")
                flow.websocket.messages[-1].drop()
                self.message_intercepted.append(InterceptedMessage(flow.request.text, flow.request.url, "Websocket"))

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
