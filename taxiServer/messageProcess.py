# -*- coding: utf-8 -*-
# @Time     : 2019/4/16 13:00
# @Author   : vickylzy

import json


# import json2table


def json_to_dict():
    j = '{"name":"lzy","age":28, "route" : [ [1,2],' \
        '[3,8]' \
        ']}'
    dic1 = json.loads(j)
    1 == 1
    return dic1


if __name__ == "__main__":
    a_list = [[12, 15], [14, 15]]

    #     content='''
    # dasdjiahdshfa
    # asdasdasdad
    # asd
    # da
    # '''.format('/')

    # paths = {
    #     '/foo': {'status': 200},
    #     '/bar': {'status': 302},
    #     '/baz': {'status': 404},
    #     '/qux': {'status': 500}
    # }

    get_dict = json_to_dict()
    # line = "127.0.0.1"
    # # line = (line, 8000)
    # line=line+':8080'
    print(get_dict)
    print(type(get_dict))
