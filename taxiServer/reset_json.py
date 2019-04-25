with open('./information.json', 'r+') as f:
    f.seek(0)
    f.truncate()
    f.write('{"current_position": [], "is_arrive_start": false, "is_in_vehicle": false,"is_reach_target": false,'
            '"is_start_nav": false,  "routine": [],"start_position": [], "target_position": []}')
