from collections import namedtuple

health_impact_ratio = namedtuple('health_impact_ratio', ['parameter', 'scoring'])

health_ratios = {
                    'co2' : {
                                'out_of_lower_bound' : health_impact_ratio(0.50, 0),
                                'good' : health_impact_ratio(0.50, 0),
                                'moderate' : health_impact_ratio(0.50, 0.25),
                                'unhealthy' : health_impact_ratio(0.50, 0.5),
                                'hazardous' : health_impact_ratio(0.50, 0.75),
                                'out_of_upper_bound' : health_impact_ratio(0.50, 1)
                            },
                    'pm2_5' : {
                                'out_of_lower_bound' : health_impact_ratio(0.30, 0),
                                'good' : health_impact_ratio(0.30, 0),
                                'moderate' : health_impact_ratio(0.30, 0.25),
                                'unhealthy' : health_impact_ratio(0.30, 0.5),
                                'hazardous' : health_impact_ratio(0.30, 0.75),
                                'out_of_upper_bound' : health_impact_ratio(0.30, 1)
                            },
                    'temp' : {
                                'out_of_lower_bound' : health_impact_ratio(0.1, 0),
                                'good' : health_impact_ratio(0.1, 0),
                                'moderate' : health_impact_ratio(0.1, 0.25),
                                'unhealthy' : health_impact_ratio(0.1, 0.5),
                                'hazardous' : health_impact_ratio(0.1, 0.75),
                                'out_of_upper_bound' : health_impact_ratio(0.1, 1)
                            },
                    'humidity' : {
                                'out_of_lower_bound' : health_impact_ratio(0.1, 0),
                                'good' : health_impact_ratio(0.1, 0),
                                'moderate' : health_impact_ratio(0.1, 0.25),
                                'unhealthy' : health_impact_ratio(0.1, 0.5),
                                'hazardous' : health_impact_ratio(0.1, 0.75),
                                'out_of_upper_bound' : health_impact_ratio(0.1, 1)
                            },
                }
