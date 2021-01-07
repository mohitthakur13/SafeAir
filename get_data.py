import urllib.request
import json
import time

from datetime import datetime, timedelta

# Constants.
API_URL = 'http://iot.orvito.com:5000/api/v1/get_device_data?session=4ea8b2ab-948a-3521-ae9e-e88c2dd60d81&device_id=1&start_date={}&end_date={}'
READ_DELAY = 59 #Interval between two API requests to check for a new reading.

pollutants_ppb = ['o3', 'no2'] # Values that are measured in ppb and need to be converted in ppm.

def api_caller(url):
    '''
    Checks if the API is working and if yes, retrieves the data.
    ''' 
    try:
        data_json = urllib.request.urlopen(url)
        past_data = json.load(data_json)
        assert(isinstance(past_data, dict)), 'The API is either not returning the data or returning not in the expected format!'
        return past_data
    except urllib.error.HTTPError as e:
        print(f'ERROR: {e}')
    except urllib.error.URLError as e:
        print(f'ERROR: {e}')


def get_reading(target):
    '''
    The 'get_reading' function constantly checks for the new readings measured by the SafeAir
    device. It does it by requesting the data from the API every 'READ_DELAY' seconds. 
    If there is a new reading, it sends it to the data stack to be queued for further processing. 
    '''
    global API_URL, READ_DELAY
    url = API_URL
    start = datetime.today().strftime('%Y-%m-%d')
    end = start
    try: 
        call = api_caller(url.format(start, end))
        current_length = len(call)
        while True:
            next_call = api_caller(url.format(start, end))
            next_length = len(next_call)
            if next_length != current_length:
                new_data = next_call['data'][0]

                for p in pollutants_ppb:
                    '''
                    Convert values from ppb to ppm.
                    '''
                    new_data[p] = new_data[p] / 1000
                
                target.send(new_data)
                current_length = next_length
            time.sleep(READ_DELAY)
    except:
        raise


def get_sample_data(target):
    '''
    Returns pre-downloaded sample data from the API.
    '''
    with open('device_data', 'rb') as f:
        data = json.load(f)['data']
    
    # Reverse the list to feed it into the LIFO stack.
    data.reverse()
    
    for point in data:
        for p in pollutants_ppb:
            '''
            Convert values from ppb to ppm.
            '''
            point[p] = point[p] / 1000
        target.send(point)
