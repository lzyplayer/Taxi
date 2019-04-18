# -*- coding: utf-8 -*-
# @Time     : 2019/4/16 11:34
# @Author   : vickylzy
import logging
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from json2html import *
from os import path

cur_dir = path.dirname(path.realpath(__file__))


# encoding data format for transform
#
# { "is_start_nav": bool,
#   "is_arrive_start": bool,
#   "is_in_vehicle": bool,
#   "is_reach_target": bool,
#   "start_position": [float, float],
#   "target_position": [float, float],
#   "current_position": [float, float],
#   "routine": [[float,float],...,[float,float]]
# }

# def __init__(self):
#     self.is_start_nav = False
#     self.is_arrive_start = False
#     self.is_in_vehicle = False
#     self.is_reach_target = False
#     self.start_position = [1.23, 1.23]
#     self.target_position = [1.23, 1.23]
#     self.current_position = [1.23, 1.23]
#     self.routine = [[1.23, 1.23], [1.23, 1.23]]


class TaxiHttpServerRequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # 当get请求时返回当前最新订单信息
        # querypath = urlparse(self.path)
        # filepath, query = querypath.path, querypath.query
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        try:
            with open(path.realpath(cur_dir + '/information.json'), 'r') as f:
                # data_taxi = json.load(f)
                data_taxi = f.read()
                content = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-a8"><title>Title</title>' \
                          '</head><body>hello</body></html>'
                data_content = content.replace('hello', json2html.convert(data_taxi))
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(data_content, 'UTF-8'))
        except IOError:
            self.send_error(404, 'json File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            get_data = self.rfile.read(int(self.headers['Content-Length']))
            got_raw_json = get_data.decode('UTF-8').replace('\\', '')
            got_dict = json.loads(got_raw_json[1:-1])
            pass #######################加油鸭！明天内搞定
            with open(path.realpath(cur_dir + '/information.json'), 'r') as f:
                # data_taxi = json.load(f)
                data_taxi = f.read()
                data_content = data_taxi
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(data_content, 'UTF-8'))
        except IOError:
            self.send_error(500, 'cannot access to json File ')
        except Exception:
            self.send_error(403, 'json sent is not in right format!')


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
    net_port = 8080
    run(server_address=net_address, port=net_port)
