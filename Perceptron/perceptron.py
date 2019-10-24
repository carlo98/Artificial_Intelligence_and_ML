import numpy as np
import math

class perceptron():
    '''
    It can classify linearly separable data.
    '''
    def __init__(self, learning_rate = 0.001):
        '''
        We create a numpy array full of zeros as weights and a scalar variable (b)
        @param learning_rate: rate at which to update the weights
        '''
        self.b = 0.0
        self.n = learning_rate

    def fit(self, X, Y):
        '''
        We create a numpy array full of zeros as weights.
        Weights are updated following the rule: w <- w + n*Yi*Xi
        Bias b is update as b <- b + n*Yi
        Where n is the learning rate, Xi an array of features and Yi the class of Xi.
        <*,*> dot product
        Pseudo-code can be found in "Perceptron.pdf".
        @param X: numpy array of input features
        @param Y: numpy array of labels associated with features (-1, 1)
        '''
        self.w = np.zeros(len(X[0]))
        iterations = 0
        cont = 0
        #It stops when perceptron compute right output for each training example
        while cont < len(Y):
            iterations += 1
            for i in range(len(Y)):
                x = X[i]
                y = Y[i]
                if y*(np.dot(x,self.w) + self.b) <= 0:
                    self.w += self.n*y*x
                    #Normalising weights
                    self.w = self.w/math.sqrt((self.w**2).sum())
                    self.b += self.n*y
                    #Wrong training example found
                    cont = 0
                else:
                    cont += 1
        print("Training completed after ",iterations," iterations.")

    def compute(self, X, probability=False):
        '''
        It computes a label for each array of features Xi; labels are 0's (class -1) or 1's (class 1)
        @param X: test features
        @param probability; if True the method will return a list of probabilities (0,1), 
                            otherwise it will return either 0 or 1 
        '''
        labels = []
        for x in X:
            z = np.dot(x, self.w) + self.b
            label = 1/(1+math.exp(-z))

            if probability:
                labels.append(label)
            elif label < 0.5:
            	labels.append(0)
            else:
                labels.append(1)
        return labels

    def _get_weights_b(self):
        '''
        It returns a dictionary with weights and bias
        '''
        return dict(weights=self.w, b=self.b)

#For given examples the line should be the x axis
X = np.array([[1,2], [2,3], [-1,2], [-4, 1], [10, 20], [-30, 14], [-3, -2], [5, -2], [-10, -30], [30, -3], [1,-3], [4, -4], [100, -9], [-0.3, 0.01], [0.02, -0.04], [0.1, 0.01]])

Y = np.zeros(len(X))
for i in range(len(X)):
    if X[i][1] < 0:
        Y[i] = -1
    else:
        Y[i] = 1

test = np.array([[1,2], [-1,2], [-2, -3], [3,-10], [100, -200], [0.1, -0.05]])

perc = perceptron()
perc.fit(X, Y)

prediction = perc.compute(test)
print(prediction)

parameters = perc._get_weights_b()
print(parameters)

