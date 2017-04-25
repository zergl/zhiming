####################################################
#        Author : zergl <e3.gemini@qq.com>
#  FisrtCreated : 2017-04-26 01:01
#  LastModified : 2017-04-26 01:01
#      Filename : zhiming.py
#   Description : 
#       History : 
#             1. First created.
#
####################################################
#!/usr/bin/env python             
#-*- coding: UTF-8 -*-             

import http.server
import socketserver

class Zhiming(object):
    def __init__(self, port=8080):
        self._port    = port
        self._handler = http.server.SimpleHTTPRequestHandler

    def serve_forever(self):
        with socketserver.TCPServer(('', self._port), self._handler) as svc:
            svc.serve_forever()

    def run(self):
        self.serve_forever()

