import requests
from retrying import  retry


@retry(stop_max_attempt_number=3)
def _parse_url():
    response = requests.get('www.baidu.com')
    assert  response.status_code == 200
    return response

def parse_url():
    try:
        response = _parse_url()
    except Exception as e:
        print(e)
        response = None
    return response
