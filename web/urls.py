#!/usr/bin/env python
#coding: utf-8
from web.handlers import main
import tornado.web

url_patterns =  [
    (r"^/$", main.IndexHandler),
    (r"^/login", main.LoginHandler),
    (r"^/logout", main.LogoutHandler),
    (r"^/index", main.IndexHandler),
    (r"^/config", main.ConfHandler),
    (r"^/proxy", main.ProxyHandler),
    (r"^/scan_config", main.ScanConfigHandler),
    (r"^/scan_stat", main.ScanStatHandler),
    (r"^/req", main.ReqHandler),
    (r"^/list", main.ListHandler),
    (r"^/del", main.DelHandler),
    (r"^/reset_scan", main.ResetScanHandler),
    (r"^/.*", main.PageNotFoundHandler),
]


