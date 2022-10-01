import imp
import os
from mitmproxy.tools.main import mitmproxy
from request_proxy.addons.http_interceptor import InterceptorHttp
from request_proxy.addons.ws_interceptor import InterceptorWs
from request_proxy.background.bg_proc import Background
from threading import Thread

# Do Initializtion method. Pull configuration from remote
# server and set up addons

t_addons = [InterceptorHttp(), InterceptorWs()]

bg_process = Background(t_addons)
thread = Thread(target=bg_process.start, args=(), daemon=True)
thread.start()

addons = t_addons
