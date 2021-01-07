import intervals as I

operational_ranges = {
    'co2' : { 
              'out_of_lower_bound' : I.open(-I.inf, 340), 
              'good' : I.closedopen(340, 600), 
              'moderate' : I.closedopen(601, 1000), 
              'unhealthy' : I.closedopen(1001, 1500), 
              'hazardous' : I.closedopen(1500, 5000),
              'out_of_upper_bound' : I.open(5000, I.inf)
            },
    'co'  : { 
              'out_of_lower_bound' : I.open(-I.inf, 0), 
              'good' : I.closedopen(0, 4.4), 
              'moderate' : I.closedopen(4.4, 9.4), 
              'unhealthy' : I.closedopen(9.5, 15.4), 
              'hazardous' : I.closedopen(15.4, 50),
              'out_of_upper_bound' : I.open(50, I.inf)
            },
    'no2' : { 
              'out_of_lower_bound' :I.open(-I.inf, 0), 
              'good' : I.closedopen(0, 0.053), 
              'moderate' : I.closedopen(0.053, 0.1), 
              'unhealthy' : I.closedopen(0.1, 1.65), 
              'hazardous' : I.closedopen(1.65, 3),
              'out_of_upper_bound' : I.open(3, I.inf)
            },
    'o3'  : { 
              'out_of_lower_bound' : I.open(-I.inf, 0), 
              'good' : I.closedopen(0, 0.060), 
              'moderate' : I.closedopen(0.060, 0.124), 
              'unhealthy' : I.closedopen(0.124, 0.404), 
              'hazardous' : I.closedopen(0.404, 1),
              'out_of_upper_bound' : I.open(1, I.inf)
            },
    'pm2_5' : { 
                'out_of_lower_bound' : I.open(-I.inf, 0), 
                'good' : I.closedopen(0, 25), 
                'moderate' : I.closedopen(25, 55), 
                'unhealthy' : I.closedopen(55, 250), 
                'hazardous' : I.closedopen(250, 500),
                'out_of_upper_bound' : I.open(500, I.inf)
              },
    'voc'  : { 
              'out_of_lower_bound' : I.open(-I.inf, 0), 
              'good' : I.closedopen(0, 100), 
              'moderate' : I.closedopen(100, 200), 
              'unhealthy' : I.closedopen(200, 350), 
              'hazardous' : I.closedopen(350, 500),
              'out_of_upper_bound' : I.open(500, I.inf)
            },
    'temp'  : { 
                'out_of_lower_bound' : None, 
                'good' : I.closedopen(20, 24), 
                'moderate' : I.closedopen(16, 20), 
                'unhealthy' : I.closedopen(24, 26), 
                'hazardous' : (I.open(-I.inf, 16), I.open(26, I.inf)), 
                'out_of_upper_bound' : None
            },
    'humidity'  : { 
                     'out_of_lower_bound' : None, 
                     'good' : I.closedopen(40, 60), 
                     'moderate' : I.closedopen(60, 80), 
                     'unhealthy' : I.closedopen(80, 90), 
                     'hazardous' : (I.open(-I.inf, 40), I.open(90, I.inf)), 
                     'out_of_upper_bound' : None
            }
    }


