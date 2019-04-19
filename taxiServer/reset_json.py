with open('./information.json', 'r+') as f:
    f.seek(0)
    f.truncate()
    f.write('{"is_start_nav": false, "is_arrive_start": false, "is_in_vehicle": false, "is_reach_target": false, '
            '"start_position": [], "target_position": [], "current_position": [], "routine": []}')
