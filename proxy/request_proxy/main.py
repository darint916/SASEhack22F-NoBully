import os
from mitmproxy.tools.main import mitmproxy
import bootstrap

mitm_exec = mitmproxy

if (__name__ == '__main__'):
    mitmproxy(args=["-s", bootstrap.__file__])
