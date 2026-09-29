import numpy as np

def f(x):
    '''
    return x ** 2
    '''
    return x ** 2

def get_func_values():
    return {x: f(x) for x in np.arange(-9 , 10).tolist()}
