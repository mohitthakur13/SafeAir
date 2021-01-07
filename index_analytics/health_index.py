from decorators.coroutine_decorator import coroutine_decorator
from index_analytics.range_queries import (get_quality,
                                           get_impact_ratio)
from index_analytics.index_pollutants.health_pollutants import INDEX, index_pollutants


def get_impact_product(pollutant, api_value):
    '''
    Gets impact ratios for a given pollutant and its api_value.
    '''
    quality = get_quality(pollutant, api_value)
    ratios = get_impact_ratio(INDEX, pollutant, quality)
    return ratios[0] * ratios[1]



@coroutine_decorator
def health_index(target=None):
    '''
    Computes health index value.
    '''
    while True:
        pollutant_impact = []
        reading = yield
        for p in index_pollutants:
            product = get_impact_product(p, reading[p])
            pollutant_impact.append(product)
        
        ieq_index_value = 100 * sum(pollutant_impact)
        target.send((INDEX, ieq_index_value, index_pollutants))
        pollutant_impact.clear()

