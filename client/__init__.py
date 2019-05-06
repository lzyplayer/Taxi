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
        # received_response = requests.get(self.url)
        self.got_json = received_response.json()


if __name__ == '__main__':
    temp_json = '{"current_position": [], "is_arrive_start": false, "is_in_vehicle": false,"is_reach_target": false,' \
                '"is_start_nav": false,  "routine": [],"start_position": [6], "target_position": [99],"velocity":0,' \
                '"gas":0,"pressure_left_front":0,"pressure_right_front":0,"pressure_left_behind":0,' \
                '"pressure_right_behind":0,"camera_status":false, "lidar_status":false,"ibeo_status":false} '
    a_client = httpClient('http://127.0.0.1:31845', temp_json)
    while True:
        a_client.do_request()
        print(a_client.got_json)
