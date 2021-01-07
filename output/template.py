'''
Expected output format:
{
    'pollutant 1' : 'reading from the sensor'
    .
    .
    .
    'pollutant k' : 'reading from the sensor'
    'data_analytics': {
            'index 1' : {
                    'pollutant 1 for index 1' : {
                            'reading' : value, 
                            'quality' : 'category', 
                            'validity' : 'out of bound or inbound'
                        }
                    .
                    .

                    'pollutant k for index 1' : named tuple (reading, quality, validity)
                }
            .
            .
            .

            'index k' : {
                    'pollutant 1 for index k' : named tuple (reading, quality, validity)
                    .
                    .
                    .
                    'pollutant m for index k' : named tuple (reading, quality, validity)
                }
            'out of bound pollutants' : ['pollutant 1', .., 'pollutant k']
            'alert' : {
                    'lower cut-off' : 'True or False',
                    'upper cut-off' : 'True or False'
                }
        }
    }
'''
