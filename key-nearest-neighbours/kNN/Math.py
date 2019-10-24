'''
Created on May 12, 2019

@author: Carlo Cena
'''
import numpy as np
def distance(data1, data2):
    '''
    It computes the euclidean distance of the two instances.
    :param: data1 and data2 are instances of data
    :return: euclidean distance
    '''
    return np.linalg.norm(data1-data2)
