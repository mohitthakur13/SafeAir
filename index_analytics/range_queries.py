from pollutant_data.operational_ranges import operational_ranges
from pollutant_data.iaqi import iaqi
from pollutant_data.ieq_impact_ratios import ieq_ratios
from pollutant_data.health_impact_ratios import health_ratios
from pollutant_data.wellness_impact_ratios import wellness_ratios
                                    

out_of_bound = ['out_of_lower_bound', 'out_of_upper_bound']
in_bound = ['good', 'moderate', 'unhealthy', 'hazardous']
impact_r ={
            'ieq' : ieq_ratios,
            'health' : health_ratios,
            'wellness' : wellness_ratios
    }



def get_pollutant_range(pollutant, quality):
    '''
    Return pollutant ranges for the in bound pollutant readings.
    '''
    if quality in in_bound:
        return (operational_ranges[pollutant][quality].lower, operational_ranges[pollutant][quality].upper)
    else:
        raise Exception(f'{pollutant} is within the category: {quality}')


def get_iaq_range(quality):
    '''
    Returns 'iaq' range for the in bound pollutant reading. 
    '''
    if quality in in_bound:
        return (iaqi[quality].lower, iaqi[quality].upper)
    else:
        raise Exception(f'{quality} not within iaq bounds.')


def get_quality(pollutant, api_value):
    '''
    Returns quality for a pollutant reading.
    '''
    categories = out_of_bound + in_bound
    for quality in categories:
        if (operational_ranges[pollutant][quality]):
            if (api_value in operational_ranges[pollutant][quality]):
                return quality
        elif api_value < operational_ranges[pollutant]['good'].lower:
            return 'out_of_lower_bound'
        else:
            return 'out_of_upper_bound'

 
def get_impact_ratio(index, pollutant, quality):
    try:
        ratios = impact_r[index][pollutant][quality]
        return (ratios.parameter, ratios.scoring)
    except:
        raise
