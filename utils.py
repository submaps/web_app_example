import numpy as np

def f(x):
    '''
    return x ** 2
    '''
    return x ** 3

def get_func_values():
    return {f(x): x for x in np.arange(-10 , 10).tolist()}
