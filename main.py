import sys

try:
    assert sys.version_info >= (3,3, 'final')
except AssertionError as e:
    print(f'Make sure that the Python with version greater than 3.3 is installed! --> {e}')



'''
Check whether the required modules are present.
'''
required_modules = ['os', 'collections', 'intervals']
import importlib.util

for package in required_modules:
    if package in sys.modules:
        continue
    elif (spec := importlib.util.find_spec(package)) is not None:
        module = importlib.util.module_from_spec(spec)
        sys.modules[package] = module
        spec.loader.exec_module(module)
        print(f'{package!r} has been imported!')
    else:
        raise Exception(f'Cannot find {package!r} module!')





from get_data import (get_reading, 
                      get_sample_data)
from data_stack import DataStack
from analytics_consolidator import AnalyticsConsolidator
from pollutant_analytics.analytics import pollutant_analytics
from index_analytics.indoor_air_quality_index import iaqi_index
from index_analytics.ieq_index import ieq_index
from index_analytics.health_index import health_index
from index_analytics.wellness_index import wellness_index
from index_analytics.analytics import index_analytics
from output.output_writer import output_writer



if __name__ == '__main__':
    ds = DataStack()                    # Create a data stack.
    a_s = AnalyticsConsolidator()       # Create the analytics consolidator.
    
    try:
        '''
        Get readings using the SafeAir API and load them to the data stack.
        ''' 
        get_reading(ds.add_item())
    except: 
        get_sample_data(ds.add_item())


    # Runs on whole test data
    while True:
        '''
        Send readings to the various index engines and to the consolidator.
        ''' 
        if not ds.is_empty():
            try:
                targets = [
                               a_s.collect_reading(), 
                               pollutant_analytics(a_s.collect_pollutant_analytics()), 
                               iaqi_index(index_analytics(a_s.collect_index_analytics())),
                               ieq_index(index_analytics(a_s.collect_index_analytics())),
                               health_index(index_analytics(a_s.collect_index_analytics())),
                               wellness_index(index_analytics(a_s.collect_index_analytics()))
                          ]
                ds.send_item(targets)
                a_s.send_analytics(output_writer())
                a_s.reset_consolidate()
            except:
                raise
        else:
            break


#    os.system('cat output/output.data')
#    os.system('rm output/output.data')



#    points = [1973, 854, 3565, 14591, 26859]
#    for point in points:
#        try:
#            targets = [
#                           a_s.collect_reading(), 
#                           pollutant_analytics(a_s.collect_pollutant_analytics()), 
#                           iaqi_index(index_analytics(a_s.collect_index_analytics())),
#                           ieq_index(index_analytics(a_s.collect_index_analytics())),
#                           health_index(index_analytics(a_s.collect_index_analytics())),
#                           wellness_index(index_analytics(a_s.collect_index_analytics()))
#                      ]
#            ds.send_item(point, targets)
#            a_s.send_analytics(output_writer())
#            a_s.reset_consolidate()
#        except:
#            raise
