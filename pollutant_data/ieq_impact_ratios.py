from collections import namedtuple

ieq_impact_ratio = namedtuple('ieq_impact_ratio', ['parameter', 'scoring'])

ieq_ratios = {
                    'co2' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.33, 0),
                                'good' : ieq_impact_ratio(0.33, 0),
                                'moderate' : ieq_impact_ratio(0.33, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.33, 0.5),
                                'hazardous' : ieq_impact_ratio(0.33, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.33, 1)
                            },
                    'co' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.011, 0),
                                'good' : ieq_impact_ratio(0.011, 0),
                                'moderate' : ieq_impact_ratio(0.011, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.011, 0.5),
                                'hazardous' : ieq_impact_ratio(0.011, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.011, 1)
                            },
                    'no2' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.011, 0),
                                'good' : ieq_impact_ratio(0.011, 0),
                                'moderate' : ieq_impact_ratio(0.011, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.011, 0.5),
                                'hazardous' : ieq_impact_ratio(0.011, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.011, 1)
                            },
                    'o3' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.011, 0),
                                'good' : ieq_impact_ratio(0.011, 0),
                                'moderate' : ieq_impact_ratio(0.011, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.011, 0.5),
                                'hazardous' : ieq_impact_ratio(0.011, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.011, 1)
                            },
                    'pm2_5' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.2, 0),
                                'good' : ieq_impact_ratio(0.2, 0),
                                'moderate' : ieq_impact_ratio(0.2, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.2, 0.5),
                                'hazardous' : ieq_impact_ratio(0.2, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.2, 1)
                            },
                    'voc' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0, 100),
                                'good' : ieq_impact_ratio(0, 100),
                                'moderate' : ieq_impact_ratio(100, 200),
                                'unhealthy' : ieq_impact_ratio(200, 350),
                                'hazardous' : ieq_impact_ratio(350, 500),
                                'out_of_upper_bound' : ieq_impact_ratio(500, 1000)
                            },
                    'temp' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.166, 0),
                                'good' : ieq_impact_ratio(0.166, 0),
                                'moderate' : ieq_impact_ratio(0.166, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.166, 0.5),
                                'hazardous' : ieq_impact_ratio(0.166, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.166, 1)
                            },
                    'humidity' : {
                                'out_of_lower_bound' : ieq_impact_ratio(0.166, 0),
                                'good' : ieq_impact_ratio(0.166, 0),
                                'moderate' : ieq_impact_ratio(0.166, 0.25),
                                'unhealthy' : ieq_impact_ratio(0.166, 0.5),
                                'hazardous' : ieq_impact_ratio(0.166, 0.75),
                                'out_of_upper_bound' : ieq_impact_ratio(0.166, 1)
                            }
                }
