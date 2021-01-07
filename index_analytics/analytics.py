from decorators.coroutine_decorator import coroutine_decorator

'''
Receives reading updated with analytics, performs alert checks and adds corresponding parameters to the
index analytics, and forwards them to the consolidator.
'''
from user_settings import (IAQI_RANGE,
                           WELNESS_INDEX_RANGE,
                           HEALTH_INDEX_RANGE,
                           INDOOR_ENVIRONMENT_RANGE,
                           THERMAL_COMFORT_RANGE)

# Index - user set ranges, mapping.
INDICES = {
             'iaqi' : IAQI_RANGE, 
             'wellness' : WELNESS_INDEX_RANGE, 
             'health' : HEALTH_INDEX_RANGE, 
             'ieq' : INDOOR_ENVIRONMENT_RANGE, 
             'thermal': THERMAL_COMFORT_RANGE
          }



@coroutine_decorator
def index_analytics(target=None):
    '''
    Receives index values from index engines.
    Uses the user settings to classify index values to an alert category. 
    Sends the analytics updated with alert analytics to the consolidator.
    '''
    while True:
        index, index_value, index_pollutants = yield
        try:
            for r in INDICES[index]:
                if index_value in INDICES[index][r]:
                    analytics = { index : {
                            'index_value' : index_value,
                            'alert_type' : r,
                            'index_pollutants' : index_pollutants
                            }
                        }
                    target.send(analytics)
        except:
            raise


        
    
