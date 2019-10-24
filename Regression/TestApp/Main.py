import numpy as np
import random
from Regressor.regressor import MyRegressor

if __name__ == '__main__':
    x = np.array([[1., 4., 3.],[5., 3., -3],[2., 5., -1.],[9., 5., 0.],[8., 2., -10.],[0., 1., 3.],[9., 10., 5.],
                  [10., 14., 1.2],[-2., 3., -4.5],[-6., -9., 1.],[20., 21., 4.],[34., 21., -10],[0., -1., 1.],[-20., -32., 0.],
                  [1., 2., -20.], [5., 6.5, 1.2],[-2., 1.6, -4.5],[-6., -6.34, 1.],[20., -9.65, 4.],[34., 21.23, -10.54],[0., -1.12, 1.11],[-20.876, -30., 0.3],
                  [0., 4., 8.],[3., 3., -5],[100., 75., -23.],[54., -120., 45.],[6., 34., -88.],[0., 1., 3.],[9., 10., 5.]])
    #Building responses
    y = []
    for row in x:
        y.append(row[0]*2+row[1]*0.5+row[2])
    #Adding errors
    y[10] = random.random()*100+1
    y[12] = random.random()*100+1
    y[2] = random.random()*100+1
    y[0] = random.random()*100+1
    y = np.array(y)
    #Testing
    my_reg = MyRegressor()
    #Reading coefficients from a file
    #my_reg.read_coeff("regressor.txt")
    my_reg.compute(x,y)
    print("Result:\n")
    print(my_reg.test([-3.,1., 1.]))
    #Printing information
    print(my_reg)
    #Storing coefficients on a file
    #my_reg.store_coeff()
   