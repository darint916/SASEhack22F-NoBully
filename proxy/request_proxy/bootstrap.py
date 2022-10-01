import os
from mitmproxy.tools.main import mitmproxy

from request_proxy.addons.basic import Counter

# Do Initializtion method. Pull configuration from remote
# server and set up addons

addons = [Counter()]
