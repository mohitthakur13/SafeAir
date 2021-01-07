from decorators.coroutine_decorator import coroutine_decorator
from index_analytics.range_queries import get_quality
'''
'''
pollutants = ['co', 'co2', 'o3', 'no2', 'pm2_5', 'voc', 'temp', 'humidity']

validity = {
        'out_of_lower_bound' : 'INVALID --> IGNORED',
        'good' : 'VALID',
        'moderate' : 'VALID',
        'unhealthy' : 'VALID',
        'hazardous' : 'VALID',
        'out_of_upper_bound' : 'INVALID --> MAX VALUE'
    }


def get_validity(quality):
    '''
    Maps quality to validity category.
    '''
    try:
        return validity[quality]
    except:
        raise


@coroutine_decorator
def pollutant_analytics(target=None):
    '''
    Computes pollutant analytics for each pollutant in the api reading and sends it to the consolidator.
    '''
    while True:
        out_of_bound_pollutants = []
        analytics = {}
        reading = yield
        for p in pollutants:
            quality = get_quality(p, reading[p])
            if quality == 'out_of_lower_bound' or quality == 'out_of_upper_bound':
                out_of_bound_pollutants.append(p)
            validity = get_validity(quality)
            analytics[p] = {
                                'quality' : quality,
                                'validity' : validity
                }
        analytics['out_of_bound'] = out_of_bound_pollutants
        target.send(analytics)
        out_of_bound_pollutants = []
        analytics = {}
