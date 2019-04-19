# -*- coding: utf-8 -*-
# @Time     : 2019/4/16 11:34
# @Author   : vickylzy

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE
mimedic = [
    ('.html', 'text/html'),
    ('.htm', 'text/html'),
    # ('.js', 'application/javascript'),
    # ('.css', 'text/css'),
    ('.json', 'application/json'),
    # ('.png', 'image/png'),
    # ('.jpg', 'image/jpeg'),
    # ('.gif', 'image/gif'),
    # ('.txt', 'text/plain'),
    # ('.avi', 'video/x-msvideo'),
]


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        querypath = urlparse(self.path)
        filepath, query = querypath.path, querypath.query

        if filepath.endswith('/'):
            filepath += 'index.html'
        ## 根据文件类型决定发送与否
        filename, fileext = path.splitext(filepath)
        for e in mimedic:
            if e[0] == fileext:
                mimetype = e[1]
                sendReply = True
                break
        try:
            with open(path.realpath(curdir + sep + filepath), 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(content)
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    # def do_POST(self):



def run():
    port = 8000
    print('starting server, port', port)

    # Server settings
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
