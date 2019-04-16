# -*- coding: utf-8 -*-
# @Time     : 2019/4/16 13:00
# @Author   : vickylzy

import json


def json_to_dict():
    j = '{"name":"lzy","age":28,' \
        '"route":[' \
        '{"s":1,"d":2},' \
        '{"s":3,"d":5}' \
        ']}'
    dic1 = json.loads(j)
    1 == 1


if __name__ == "__main__":
    json_to_dict()
