"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx
from mitmproxy import http

class Counter:
    def __init__(self):
        self.num = 0

    def websocket_start(self, flow: http.HTTPFlow):
        # ctx.log.alert(f"A WS Connection has been commenced. HOST: {flow.request.host}")
        return

    def websocket_message(self, flow: http.HTTPFlow):
        # ctx.log.alert(f"A WS Message has been posted. {flow}")
        msg = flow.websocket.messages[-1]
        ctx.log.alert(msg)

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
