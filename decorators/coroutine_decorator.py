def coroutine_decorator(func):
    '''
    Initiates the coroutine with the next method.
    '''
    def start(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c
    return start
