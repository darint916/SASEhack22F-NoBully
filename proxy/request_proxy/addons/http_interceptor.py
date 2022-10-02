from ctypes import util
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
from request_proxy.model.predict import predict, model

class InterceptorHttp(IMitmProxyAddon):

    def __init__(self):
        self._activated = True
        self.config: Config = Config()
        self.message_intercepted: List[InterceptedMessage] = []
        self.blocked_word = []

    def response(self, flow: http.HTTPFlow) -> None:
        if (not self._activated):
            return

        if (utils.match_url(self.config.domains, flow.request.url)):
            # ctx.log.error(flow.response)
            if (not flow.response):
                return
            # ctx.log.error(f"Intercepted request: {flow.request.url}")
            if (utils.match_word(self.config.blockedWords, flow.response.get_text(False))):
                # ctx.log.error(f"Request intercepted. {flow.request.}")
                if ('instagram' in flow.request.url):
                    return
                flow.kill()
                if ("twitter" in flow.request.url):
                    ctx.log.error(utils.extract_twitter(flow.response.get_text(False)))
                    self.message_intercepted.append(InterceptedMessage(
                        utils.extract_twitter(flow.response.get_text(False)),
                        flow.request.url,
                        "Blocked word"
                    ))
                self.message_intercepted.append(InterceptedMessage(flow.response.text, flow.request.url, "Request"))

            if ("twitter" in flow.request.url):
                msg = utils.extract_twitter(flow.response.get_text(False))
                # ctx.log.error(msg)
                bl = predict(msg, model)
                if (bl == "not bullying"):
                    return
                self.message_intercepted.append(InterceptedMessage(
                    utils.extract_twitter(flow.response.get_text(False)),
                    flow.request.url,
                    f"AI-{bl}"
                ))
                try:
                    flow.kill()
                    ctx.log.error(f"AI-{bl} {msg}")
                except:
                    pass

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
