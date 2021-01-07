from collections import namedtuple

wellness_impact_ratio = namedtuple('wellness_impact_ratio', ['parameter', 'scoring'])

wellness_ratios = {
                    'co2' : {
                                'out_of_lower_bound' : wellness_impact_ratio(0.25, 0),
                                'good' : wellness_impact_ratio(0.25, 0),
                                'moderate' : wellness_impact_ratio(0.25, 0.25),
                                'unhealthy' : wellness_impact_ratio(0.25, 0.5),
                                'hazardous' : wellness_impact_ratio(0.25, 0.75),
                                'out_of_upper_bound' : wellness_impact_ratio(0.25, 1)
                            },
                    'pm2_5' : {
                                'out_of_lower_bound' : wellness_impact_ratio(0.25, 0),
                                'good' : wellness_impact_ratio(0.25, 0),
                                'moderate' : wellness_impact_ratio(0.25, 0.25),
                                'unhealthy' : wellness_impact_ratio(0.25, 0.5),
                                'hazardous' : wellness_impact_ratio(0.25, 0.75),
                                'out_of_upper_bound' : wellness_impact_ratio(0.25, 1)
                            },
                    'voc' : {
                                'out_of_lower_bound' : wellness_impact_ratio(0.25, 0),
                                'good' : wellness_impact_ratio(0.25, 0),
                                'moderate' : wellness_impact_ratio(0.25, 0.25),
                                'unhealthy' : wellness_impact_ratio(0.25, 0.5),
                                'hazardous' : wellness_impact_ratio(0.25, 0.75),
                                'out_of_upper_bound' : wellness_impact_ratio(0.25, 1)
                            },
                    'temp' : {
                                'out_of_lower_bound' : wellness_impact_ratio(0.125, 0),
                                'good' : wellness_impact_ratio(0.125, 0),
                                'moderate' : wellness_impact_ratio(0.125, 0.25),
                                'unhealthy' : wellness_impact_ratio(0.125, 0.5),
                                'hazardous' : wellness_impact_ratio(0.125, 0.75),
                                'out_of_upper_bound' : wellness_impact_ratio(0.125, 1)
                            },
                    'humidity' : {
                                'out_of_lower_bound' : wellness_impact_ratio(0.125, 0),
                                'good' : wellness_impact_ratio(0.125, 0),
                                'moderate' : wellness_impact_ratio(0.125, 0.25),
                                'unhealthy' : wellness_impact_ratio(0.125, 0.5),
                                'hazardous' : wellness_impact_ratio(0.125, 0.75),
                                'out_of_upper_bound' : wellness_impact_ratio(0.125, 1)
                            },
                }
