'''
Contains constants and variable ranges that are used to compute the indices.
Packages required: python-intervals.
'''
import intervals as I
from collections import namedtuple





ieq_impact_ratios = namedtuple('ieq_impact_ratios', ['parameter', 'scoring'])
wellness_impact_ratios = namedtuple('wellness_impact_ratios', ['parameter', 'scoring'])
health_impact_ratios = namedtuple('health_impact_ratios', ['parameter', 'scoring'])
pollutant_data = namedtuple('pollutant_data', ['iaq', 'ieq', 'wellness', 'health'])

IAQI = {
    'co' : {
        'out_of_lower_bound' : I.closedopen(-I.inf, 0),
        'good' : I.closed(0, 4.4),
        'moderate' : I.openclosed(4.4, 9.4),
        'unhealthy' : I.openclosed(9.4, 15.4),
        'hazardous' : I.openclosed(15.4, 50),
        'out_of_upper_bound' : I.openclosed(50, I.inf)
        },

    'no2' : {
        'out_of_lower_bound' : I.closedopen(-I.inf, 0),
        'good' : I.closed(0, 0.053),
        'moderate' : I.openclosed(0.053, 0.1),
        'unhealthy' : I.openclosed(0.1, 1.65),
        'hazardous' : I.openclosed(1.65, 3),
        'out_of_upper_bound' : I.openclosed(3, I.inf)
        },

    'o3' : {
        'out_of_lower_bound' : I.closedopen(-I.inf, 0),
        'good' : I.closed(0, 0.06),
        'moderate' : I.openclosed(0.06, 0.125),
        'unhealthy' : I.openclosed(0.125, 0.405),
        'hazardous' : I.openclosed(0.405, 1.0),
        'out_of_upper_bound' : I.openclosed(1, I.inf)
        },

    'pm2_5' : {
        'out_of_lower_bound' : I.closedopen(-I.inf, 0),
        'good' : I.closed(0, 25),
        'moderate' : I.openclosed(25, 55),
        'unhealthy' : I.openclosed(55, 250),
        'hazardous' : I.openclosed(250, 500),
        'out_of_upper_bound' : I.openclosed(500, I.inf)
        },

    'voc' : {
        'out_of_lower_bound' : I.closedopen(-I.inf, 0),
        'good' : I.closed(0, 100),
        'moderate' : I.openclosed(100, 200),
        'unhealthy' : I.openclosed(200, 350),
        'hazardous' : I.openclosed(350, 500),
        'out_of_upper_bound' : I.openclosed(500, I.inf)
        },

    'iaq' : {
        'out_of_lower_bound' : I.closedopen(-I.inf, 0),
        'good' : I.closed(0, 25),
        'moderate' : I.openclosed(25, 50),
        'unhealthy' : I.openclosed(50, 75),
        'hazardous' : I.openclosed(75, 100),
        'out_of_upper_bound' : I.openclosed(100, I.inf)
        }
    }

IEQ = {
        '''
        pollutant : { range : { quality : pollutant_data }}
        '''
        'co2' : {
                    I.open(-I.inf, 340) :      {
                                                 'out_of_lower_bound' : None,
                                               },
                    I.closedopen(340, 600) :   {
                                                 'good' : pollutant_data(0.33, 0, None)
                                               },
                    I.closedopen(600, 1000) :  {
                                                 'moderate' : pollutant_data(0.33, 0.25, None),
                                               },
                    I.closedopen(1000, 1500) : {
                                                 'unhealthy' : pollutant_data(0.33, 0.5, None),
                                               },
                    I.closed(1500, 5000) :     {
                                                 'hazardous' : pollutant_data(0.33, 1, None)
                                               },
                    I.open(5000, I.inf) :      {
                                                'out_of_upper_bound' : None
                                               }
            },
        'co' : {
                    I.open(-I.inf, 0) :      {
                                                 'out_of_lower_bound' : None,
                                               },
                    I.closedopen(0, 4.4) :   {
                                                 'good' : pollutant_data(0.011, 0, I.closed(0, 25))
                                               },
                    I.closedopen(4.4, 9.4) :  {
                                                 'moderate' : pollutant_data(0.011, 0.25, I.closed(25, 50)),
                                               },
                    I.closedopen(9.4, 15.4) : {
                                                 'unhealthy' : pollutant_data(0.011, 0.5, I.closed(50, 75)),
                                               },
                    I.closed(15.4, 50) :     {
                                                 'hazardous' : pollutant_data(0.011, 1, I.closed(75, 100))
                                               },
                    I.open(50, I.inf) :      {
                                                'out_of_upper_bound' : None
                                               }
            },
        'no2' : {
                    I.open(-I.inf, 0.053) :      {
                                                 'out_of_lower_bound' : None,
                                               },
                    I.closedopen(0.053, 0.1) :   {
                                                 'good' : pollutant_data(0.011, 0, I.closed(0, 25))
                                               },
                    I.closedopen(4.4, 9.4) :  {
                                                 'moderate' : pollutant_data(0.011, 0.25, I.closed(25, 50)),
                                               },
                    I.closedopen(9.4, 15.4) : {
                                                 'unhealthy' : pollutant_data(0.011, 0.5, I.closed(50, 75)),
                                               },
                    I.closed(15.4, 50) :     {
                                                 'hazardous' : pollutant_data(0.011, 1, I.closed(75, 100))
                                               },
                    I.open(50, I.inf) :      {
                                                'out_of_upper_bound' : None
                                               }
            },
        'o3' : {
                    I.open(-I.inf, 0.060) :      {
                                                 'out_of_lower_bound' : None,
                                               },
                    I.closedopen(0, 0.060) :   {
                                                 'good' : pollutant_data(0.011, 0, I.closed(0, 25))
                                               },
                    I.closedopen(0.060, 0.124) :  {
                                                 'moderate' : pollutant_data(0.011, 0.25, I.closed(25, 50)),
                                               },
                    I.closedopen(0.124, 0.404) : {
                                                 'unhealthy' : pollutant_data(0.011, 0.5, I.closed(50, 75)),
                                               },
                    I.closed(0.404, 1) :     {
                                                 'hazardous' : pollutant_data(0.011, 1, I.closed(75, 100))
                                               },
                    I.open(1, I.inf) :      {
                                                'out_of_upper_bound' : None
                                               }
            },
    }
