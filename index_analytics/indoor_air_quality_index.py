from decorators.coroutine_decorator import coroutine_decorator
from index_analytics.range_queries import (get_pollutant_range,
                                   get_iaq_range,
                                   get_quality)
from index_analytics.index_pollutants.iaqi_pollutants import INDEX, MAX_IAQI_VALUE, index_pollutants 


def get_index_value(reading):
    '''
    Computes iaq index value and returns it to the caller.
    '''
    p_indices = {}
    for p in index_pollutants:
        quality = get_quality(p, reading[p])
        if quality == 'out_of_lower_bound':
            continue    # Ignore the api_value and therefore the pollutant index.
        elif quality == 'out_of_upper_bound':
            p_indices[p] = MAX_IAQI_VALUE    # Out of bound index implies max iaq value. For details check
                                             # with air quality scientists. 
        else:
            r = get_pollutant_range(p, quality)
            q = get_iaq_range(quality)
            p_diff = r[1] - r[0]
            q_diff = q[1] - q[0]
            diff_ratio = q_diff / p_diff
            diff = reading[p] - r[0]
            index_value = (diff_ratio * diff) + q[0]
            p_indices[p] = index_value

    iaq_index_value = max(p_indices.values())
    return iaq_index_value



@coroutine_decorator
def iaqi_index(target=None):
    '''
    The calculator function receives a reading and uses indoor air quality index formula to compute the index
    value. The function then sends the index value to the alert checker.
    Steps:
        0. Receive reading from the data stack.
        1. Compute iaqi_index_value using compute_iaqi function on the computation data structure.
        2. Sends the result to the analytics engine (Alert classifier).
    '''
    while True:
        reading = yield
        if isinstance(reading, dict):
            try:
                iaqi_index_value = get_index_value(reading)
                target.send((INDEX, iaqi_index_value, index_pollutants))
            except: 
                raise
        else:
            print(f'{reading} is not a python dictionary.')
