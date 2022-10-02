from typing import Dict, List
from mitmproxy import ctx
from mitmproxy import http
from mitmproxy.websocket import WebSocketMessage
from request_proxy.addons.utils import utils
from request_proxy.addons.utils.config import Config
from request_proxy.interface.IMitmProxyAddon import IMitmProxyAddon
from request_proxy.InterceptedMessage import InterceptedMessage
from request_proxy.model.predict import predict, model

class InterceptorWs(IMitmProxyAddon):

    def __init__(self):
        self._activated = True
        self.config: Config = Config()
        self.message_intercepted: List[InterceptedMessage] = []
        self.blocked = []

    def websocket_message(self, flow: http.HTTPFlow):
        if (not self._activated):
            return

        # ctx.log.error(f"Websocket message intercepted --. {flow.request.url}")
        if (utils.match_url(self.config.domains, flow.request.url)):
            msg = flow.websocket.messages[-1].content
            try:
                msg_idx = msg.index(b'[')
            except ValueError:
                return

            msg_decoded = msg[msg_idx:].decode('utf-8')
            # ctx.log.alert()
            if (utils.match_word(self.config.blockedWords, msg_decoded) or utils.match_word(self.blocked, msg_decoded)):
                ctx.log.error(f"Websocket message intercepted --. {flow.request.url}")
                flow.websocket.messages[-1].drop()
                if ("instagram" in flow.request.url):
                    sent_msg = utils.extract_insta(msg_decoded)
                if (sent_msg == ''):
                    return;
                icpt = InterceptedMessage(sent_msg, flow.request.url, "Blocked Word")
                self.message_intercepted.append(icpt)
                ctx.log.error(f"Intercepted message: {icpt.to_dict()}")

            if ("instagram" in flow.request.url):
                sent_msg = utils.extract_insta(msg_decoded)
                if (sent_msg == ""):
                    return
                bl = predict(sent_msg, model)
                if (bl == "not bullying"):
                    return
                flow.websocket.messages[-1].drop()
                self.blocked.append(sent_msg)
                icpt = InterceptedMessage(sent_msg, flow.request.url, f"AI-{bl}")
                self.message_intercepted.append(icpt)
                ctx.log.error(f"AI Intercepted message: {icpt.to_dict()}")

    def report(self) -> Dict[str, str]:
        return {
            'name': self.addon_name(),
            'activated': self.is_activated(),
            'intercepted': [i.to_dict() for i in self.message_intercepted]
        }

    def use_config(self, config):
        self.config.load_cfg(config)
        ctx.log.error(f"Config received: {config}")

    def activate(self, activate: bool):
        self._activated = activate
        
    def is_activated(self) -> bool:
        return self._activated

    def addon_name(self) -> str:
        return "Websocket Interceptor"
