# -*- coding: utf-8 -*-
# @Time     : 2019/4/18 20:05
# @Author   : vickylzy
import requests


class httpClient:
    def __init__(self, input_url, input_jdata):
        self.url = input_url
        self.json_data = input_jdata
        self.got_json = ''

    def do_request(self):
        received_response = requests.post(self.url, json=self.json_data)
        self.got_json = received_response.json()


if __name__ == '__main__':
    temp_json = '{ ' \
                '"is_start_nav": false,' \
                '"is_arrive_start": false,' \
                '"is_in_vehicle": false,' \
                '"is_reach_target": false,' \
                '"start_position": [1.23, 1.23],' \
                '"target_position": [1.23, 1.23],' \
                '"current_position": [1.23, 1.23],' \
                '"routine": [[1.23,1.23],[1.23,1.23]]' \
                '}'
    a_client = httpClient('http://127.0.0.1:8080', temp_json)
    a_client.do_request()
    print(a_client.got_json)