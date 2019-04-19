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
    with open('./information.json', 'r') as f:
        # data_taxi = json.load(f)
        data_taxi = f.read()
        data_content = json.loads(data_taxi)


    # a_list = [[12, 15], [14, 15]]
    if not data_content['start_position'] and not data_content['target_position']:
        print(data_content)
        print(type(data_content))
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

    # get_dict = json_to_dict()
    # line = "127.0.0.1"
    # # line = (line, 8000)
    # line=line+':8080'
    # print(data_content)
    # print(type(data_content))
