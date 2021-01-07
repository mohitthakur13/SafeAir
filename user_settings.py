import intervals as I
'''
User defined cut-off levels for the indices.
'''

IAQI_RANGE = {
    'out_of_lower_bound' : I.open(-I.inf, 0),
    'in_operational_range' : I.closed(0, 50),
    'out_of_upper_bound' : I.open(50, I.inf)
    }


THERMAL_COMFORT_RANGE = {
    'out_of_lower_bound' : I.open(-I.inf, 20),
    'in_operational_range' : I.closed(20, 80),
    'out_of_upper_bound' : I.open(80, I.inf)
    }


HEALTH_INDEX_RANGE = {
    'out_of_lower_bound' : I.open(-I.inf, 0),
    'in_operational_range' : I.closed(0, 50),
    'out_of_upper_bound' : I.open(50, I.inf)
    }


INDOOR_ENVIRONMENT_RANGE = {
    'out_of_lower_bound' : I.open(-I.inf, 0),
    'in_operational_range' : I.closed(0, 50),
    'out_of_upper_bound' : I.open(50, I.inf)
    }


WELNESS_INDEX_RANGE = {
    'out_of_lower_bound' : I.open(-I.inf, 0),
    'in_operational_range' : I.closed(0, 50),
    'out_of_upper_bound' : I.open(50, I.inf)
    }
