from decorators.coroutine_decorator import coroutine_decorator
from output.output_writer import output_writer


class AnalyticsConsolidator():
    '''
    The data structure consolidates several index analytics and combines them to create the output.
    '''
    def __init__(self):
        self.consolidate = {}
    
    @coroutine_decorator
    def collect_reading(self):
        '''
        Collects the reading from the data stack.
        '''
        while True:
            reading = yield
            self.consolidate = reading
            self.consolidate['data_analytics'] = {
                    'pollutant_analytics' : {},
                    'index_analytics' : {}
                }

    @coroutine_decorator
    def collect_pollutant_analytics(self):
        '''
        Collects the index analytics from respective index calculators.
        '''
        while True:
            analytics = yield
            for key in analytics.keys():
                self.consolidate['data_analytics']['pollutant_analytics'][key] = analytics[key]
    
    @coroutine_decorator
    def collect_index_analytics(self):
        '''
        Collects the index analytics from respective index calculators.
        '''
        while True:
            analytics = yield
            for key in analytics.keys():
                self.consolidate['data_analytics']['index_analytics'][key] = analytics[key]

    def send_analytics(self, target):
        '''
        Sends the collected data analytics for the corresponding reading to the output.
        '''
        target.send(self.consolidate)

    def reset_consolidate(self):
        self.consolidate.clear()

    def print_analytics(self): 
        print(self.consolidate)
