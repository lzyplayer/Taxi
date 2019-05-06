# -*- coding: utf-8 -*-
# @Time     : 2019/4/16 11:34
# @Author   : vickylzy
import logging
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from json2html import *
from os import path
from socketserver import ThreadingMixIn

cur_dir = path.dirname(path.realpath(__file__))

# encoding data format for transform
#
# { "is_start_nav": bool,				user control
#   "is_arrive_start": bool,				taxi control
#   "is_in_vehicle": bool,				user control
#   "is_reach_target": bool,				taxi(to false)/user(to true) control
#   "start_position": [float, float],			user control
#   "target_position": [float, float],			user control
#   "current_position": [float, float],			taxi control
#   "routine": [[float,float],...,[float,float]],       taxi control
#   "velocity": float                   taxi control
#   "gas": float                        taxi control
#   "pressure_left_front": float        taxi control
#   "pressure_right_front": float        taxi control
#   "pressure_left_behind": float        taxi control
#   "pressure_right_behind": float        taxi control
#   "camera_status": bool               taxi control
#   "lidar_status": bool                taxi control
#   "ibeo_status": bool                  taxi control
# }
dataLock = threading.Lock()
with open('./information.json', 'r') as glaFile:
    freshJson = json.load(glaFile)

message_type = [('/', 'text/html'),
                ('/favicon.ico', 'image/x-icon'),
                ('/information.json', 'text/html')]


class TaxiHttpServerRequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # 当get请求时返回当前最新订单信息
        acquire_path = self.path
        response_type = ''
        for atype in message_type:
            if acquire_path == atype[0]:
                response_type = atype[1]
                break
        # if acquire_path == '/':
        #     acquire_path = acquire_path + 'information.json'
        logging.info("GET request,Path: %s", str(self.path))
        try:
            if response_type == '':
                raise IOError
            self.send_response(200)
            self.send_header('Content-type', response_type)
            self.end_headers()
            if acquire_path == '/' or acquire_path == '/?':
                data_taxi = json.dumps(freshJson)
                content = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-a8"><title>Xian Jiao Tong ' \
                          'pioneer taxi Service</title>' \
                          '</head><body>hello</body></html>'
                data_content = content.replace('hello', json2html.convert(data_taxi))
                self.wfile.write(bytes(data_content, 'UTF-8'))
            elif acquire_path == '/favicon.ico':
                with open('.' + acquire_path, 'rb') as f:
                    self.wfile.write(f.read())
            elif acquire_path == '/information.json':
                self.wfile.write(bytes(json.dumps(freshJson), 'UTF-8'))
        except IOError:
            self.send_error(404, ' File Not Found: %s' % acquire_path)

    def do_POST(self):
        # 解析传入json
        logging.info("get a post")
        sender = ''
        trim_dict = ''
        try:
            get_data = self.rfile.read(int(self.headers['Content-Length']))
            got_raw_json = get_data.decode('UTF-8').replace('\\', '')
            start_pos = got_raw_json.find('{')
            end_pos = got_raw_json.find('}')
            got_dict = json.loads(got_raw_json[start_pos:end_pos + 1])  # [1:-1]
            sender, trim_dict = check_sender(got_dict)
        except Exception:
            self.send_error(403, 'json sent is not in right format!')
        try:
            if sender:
                dataLock.acquire()
                freshJson.update(trim_dict)
                dataLock.release()
                logging.info("Update a Post from %s", sender)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(freshJson), 'UTF-8'))
        except Exception:
            self.send_error(500, 'server wrong ')


def check_sender(send_in_dict):
    require_keys = ["is_start_nav", "is_arrive_start", "is_in_vehicle", "is_reach_target", "start_position",
                    "target_position", "current_position", "routine", "velocity", "gas", "pressure_left_front",
                    "pressure_right_front", "pressure_left_behind", "pressure_right_behind", "camera_status",
                    "lidar_status", "ibeo_status"]
    has_keys = send_in_dict.keys()
    for key in require_keys:
        if key not in has_keys:
            raise Exception
    if not send_in_dict["start_position"] and not send_in_dict["target_position"]:
        del send_in_dict["start_position"]
        del send_in_dict["target_position"]
        del send_in_dict["is_start_nav"]
        del send_in_dict["is_in_vehicle"]
        if not send_in_dict["is_reach_target"]:
            del send_in_dict["is_reach_target"]
        return 'taxi', send_in_dict
    elif not send_in_dict["current_position"] and not send_in_dict["routine"]:
        del send_in_dict["current_position"]
        del send_in_dict["routine"]
        del send_in_dict["is_arrive_start"]
        del send_in_dict["velocity"]
        del send_in_dict["gas"]
        del send_in_dict["pressure_left_front"]
        del send_in_dict["pressure_right_front"]
        del send_in_dict["pressure_left_behind"]
        del send_in_dict["pressure_right_behind"]
        del send_in_dict["camera_status"]
        del send_in_dict["lidar_status"]
        del send_in_dict["ibeo_status"]
        if send_in_dict["is_reach_target"]:
            del send_in_dict["is_reach_target"]
        # del send_in_dict["is_reach_target"]
        return 'user', send_in_dict
    raise Exception

    # multiThread part


class ThreadingHttpServer(ThreadingMixIn, HTTPServer):
    pass


def run(server_class=TaxiHttpServerRequestHandler, server_address='', port=8000):
    # log configured
    logging.basicConfig(level=logging.INFO)
    # server
    server_address = (server_address, port)
    httpd = ThreadingHttpServer(server_address, server_class)
    # httpd = HTTPServer(server_address, server_class)
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
    net_port = 31845
    run(server_address=net_address, port=net_port)

# def __init__(self):
#     self.is_start_nav = False
#     self.is_arrive_start = False
#     self.is_in_vehicle = False
#     self.is_reach_target = False
#     self.start_position = [1.23, 1.23]
#     self.target_position = [1.23, 1.23]
#     self.current_position = [1.23, 1.23]
#     self.routine = [[1.23, 1.23], [1.23, 1.23]]

# # 返回数据
# self.send_response(200)
# self.send_header('Content-type', 'text/html')
# self.end_headers()
# self.wfile.write(bytes(data_content, 'UTF-8'))
