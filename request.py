import requests
import json


import pandas as pd

url = 'http://127.0.0.1:5000/predict/'

# The format of the sent data should be as follow : 

# ~> "duration","codec","width","height","bitrate","framerate","i","p","b","frames","i_size","p_size","b_size","size","o_codec","o_bitrate","o_framerate","o_width","o_height","umem"


# Transforming a 3 min video from 480p in flv to 4K in mpeg4 while allocating 58.5 MB in umem

# Careful, the FPS should be equal to number of frames / duration (in seconds)

request_test = [180,"flv",480,360,550000,30,250,5000,150,5400,2000,85000,1000,88000,"mpeg4",56000,60,3840,2160,58528]

jsonyfied_data = json.dumps(request_test)

headers = {
            'content-type': 'application/json', 
            'Accept-Charset': 'UTF-8'
            }

response = requests.post(url, data=jsonyfied_data, headers=headers)

print(f"The response code is {response.status_code} \n\nIt will be transcoded in {response.json()['result']} seconds.")