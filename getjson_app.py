import requests
import json
from requests.exceptions import HTTPError
import getjson_manager

try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    json_data = json.loads(response.text)
    
    key = int(input("1. แสดงข้อมูลทั้งหมด 2. แสดงข้อมูลตามหมายเลข ID : "))
    
    getjson_manager.getjson(key, json_data)
    
        
    
except HTTPError as http_err:
    print(f'HTTP error : {http_err}')
except Exception as err:
    print(f'Other error : {err}')