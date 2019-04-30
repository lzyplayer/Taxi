with open('./information.json', 'r+') as f:
    f.seek(0)
    f.truncate()
    f.write('{"current_position": [], "is_arrive_start": false, "is_in_vehicle": false,"is_reach_target": false,'
            '"is_start_nav": false,  "routine": [],"start_position": [], "target_position": [],"velocity":0,"gas":0,'
            '"pressure_left_front":0,"pressure_right_front":0,"pressure_left_behind":0,"pressure_right_behind":0,'
            '"camera_status":false, "lidar_status":false,"ibeo_status":false'
            '}')


