import time
from typing import List
from request_proxy.interface.IMitmProxyAddon import IMitmProxyAddon
from request_proxy.background.api_client import ApiClient
import traceback

from mitmproxy import ctx

class Background:

    def __init__(self, addons: List[IMitmProxyAddon]) -> None:
        self.addons = addons
        self.api = ApiClient("http://10.8.0.4:7000")
        self.last_config = None

    def report(self):
        report = {}
        for addon in self.addons:
            report[addon.addon_name()] = addon.report()
            ctx.log.error(f"Report: {report}")
        self.api.post_report(report)

    def pull_cfg(self):
        config = self.api.get_config()
        if (config != self.last_config):
            self.last_config = config
            for addon in self.addons:
                addon.use_config(config)

    def _write_dbg_file(self, msg):
        with open("dbg.txt", "a") as f:
            f.write(msg + "\n")

    def start(self):
        while True:
            try:
                self.pull_cfg()
                time.sleep(30)
                self.report()
            except Exception as e:
                data = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                self._write_dbg_file(data + "\n")
