'''
Created on Apr 29, 2019

@author: Carlo Cena
'''
import numpy as np
from numpy import double

class MyRegressor(object):
    '''
    It builds a linear regressor.
    '''

    def compute(self, x_set, y_set):
        '''
        :param: x_set and y_set: sub-set of input data
        It uses the Least Square method to minimize the residual error
        Please look at the documentation for more detailed information
        '''
        self.a = np.dot(np.dot(np.linalg.inv(np.dot(x_set.T,x_set)),x_set.T),y_set)

    def __str__(self):
        return "Regression coefficients: " + str(self.a)
        
    def test(self, x_test):
        return np.dot(self.a,x_test)    
    
    def store_coeff(self):
        '''
        Writing coefficients on a file
        '''
        try:
            my_file = open("regressor.txt",'w')
            for num in self.a:
                my_file.write(str(num))
        except IOError:
            print("*** file open error.")
            
    def read_coeff(self, file):
        '''
        Reading coefficients from file
        '''
        try:
            my_file = open(file, 'r')
            self.a = []
            for num in my_file.read():
                self.a.append(double(num))
            self.a = np.array(self.a)
        except IOError:
            print("*** file open error.")
            
     
                
                