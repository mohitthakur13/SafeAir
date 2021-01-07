from decorators.coroutine_decorator import coroutine_decorator
from pollutant_data.ppb_pollutants import ppb_pollutants


class DataStack(object):
    '''
    LIFO data structure prioritizing latest added data over last.
    Basic methods.
    '''
    def __init__(self):
        self.stack = []

    @coroutine_decorator
    def add_item(self):
        '''
        A coroutine that appends item to the stack and remembers the state.
        '''
        while True:
            item = yield
            self.stack.append(item)

    def get_item(self, position):
        '''
        Returns the kth (position) item from the stack.
        '''
        try:
            item = self.stack[position]
            return item
        except IndexError as e:
            print(f'Stack IndexError: {e}')


    def send_item(self, targets):
        '''
        Pops the reading from the data stack.
        Converts the ppb pollutant api values to ppm.
        Sends the updated reading to the target function.
        '''
        try:
            item = self.stack.pop()
            
            for index in ppb_pollutants:
                item[index] = self.ppb_to_ppm(item[index])
            
            for target in targets:
                target.send(item)
        except IndexError:
            print(f'The data stack is empty!')

    
    def ppb_to_ppm(self, api_value):
        '''
        Converts ppb pollutant api values to ppm.
        '''
        if isinstance(api_value, (int, float)):
            return api_value / 1000
        else:
            raise Exception(f'{api_value} is not a number!')
     

    def size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False




#    def send_item(self, position, targets):
#        try:
#            item = self.get_item(position)
#            for target in targets:
#                target.send(item)
#        except:
#            raise
