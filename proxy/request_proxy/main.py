import os
from mitmproxy.tools.main import mitmweb
import bootstrap

mitm_exec = mitmweb

if (__name__ == '__main__'):
    mitmweb(args=["-s", bootstrap.__file__])
