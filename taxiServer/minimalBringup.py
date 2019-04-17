# -*- coding: utf-8 -*-
# @Time     : 2019/4/16 11:34
# @Author   : vickylzy
import logging
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse

curdir = path.dirname(path.realpath(__file__))
# sep = '/'

class TaxiHttpServerRequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # 当get请求时返回当前最新订单信息
        # querypath = urlparse(self.path)
        # filepath, query = querypath.path, querypath.query
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        try:
            with open(path.realpath(curdir + '/information.json'), 'r') as f:
                # data_taxi = json.load(f)
                data_taxi = f.read()
                content = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-a8"><title>Title</title>' \
                          '</head><body>hello</body></html>'
                data_content = content.replace('hello', data_taxi)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(data_content, 'UTF-8'))
        except IOError:
            self.send_error(404, 'json File Not Found: %s' % self.path)

    # def do_POST(self):



def run(server_class=TaxiHttpServerRequestHandler, server_address='', port=8000):
    # log configured
    logging.basicConfig(level=logging.INFO)
    # server
    server_address = (server_address, port)
    httpd = HTTPServer(server_address, server_class)
    logging.info("starting httpServer on %s  ...", server_address)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("closed httpServer on %s !", server_address)


if __name__ == '__main__':
    # start service
    net_address = ''
    net_port = 8000
    run(server_address=net_address, port=net_port)
