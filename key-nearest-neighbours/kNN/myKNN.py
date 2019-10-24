'''
Created on May 12, 2019

@author: Carlo Cena
'''
from kNN.Math import distance
from collections import Counter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class myKNN(object):
    '''
    Implementation of key-nearest-neighbour, 
    the ranking of the neighbors is based on their distance from the input.
    It is available a method that prints a 3D-plot of the input data.
    '''

    def __init__(self, data, labels, K=3):
        '''
        :param: data: Training data
        :param: labels: Labels of the training data
        :param: K: optional parameter, it defines the number of neighbours
                default: 3
        It just makes a copy of the data and set the value of K
        '''
        if data is not None:
            self.data = data
        else:
            print("*** Missing parameter: \"data\"\n")
        if labels is not None:
            self.labels = labels
        else:
            print("*** Missing parameter: \"labels\"\n")
        self.K = K
        
    def find_neighbours(self, test_data_instance):
        '''
        "find_neighbours" finds the self.K nearest neighbors of an instance
        of test data.
        :param: test_data_instance
        :return: neighbors: 3-tuples (index, dist, label)
        index: index from the training set
        dist: distance between the instance and the instance
                of the training set
        '''
        neighbours = []
        for i in range(len(self.data)):
            dist = distance(test_data_instance, self.data[i])
            neighbours.append((i, dist, self.labels[i]))
        neighbours.sort(key=lambda x: x[1])
        return neighbours[:self.K]
    
    def vote_distance_weight(self, neighbours):
        '''
        The label of each instance is compute by using the distances of 
        his neighbours.
        '''
        class_counter = Counter()
        for index in range(len(neighbours)):
            dist = neighbours[index][1]
            label = neighbours[index][2]
            class_counter[label] += 1 / (dist**2 + 1)
        winner = class_counter.most_common(1)[0][0]
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
            class_counter[key] /= total
        return winner, class_counter.most_common()
    
    def plot(self, predictions, test_data, test_labels, print_all = False):
        '''
        :param: predictions: predicted labels
        :param: test_data 
        :param: test_labels
        :param: print_all = False : whether or not to print both training and test data
        Colors:
        red:   case (print_all=False) -> correct labels
               case (print_all=True) -> training data
        green: case (print_all=False) -> wrong labels
               case (print_all=True) -> training data
        yellow: training
        black: correct label
        magenta: wrong label
        Please work on the code in order for it to work better with your data
        '''
        colours = ("r", "g", "y","k","m")
        X = []
        N = 2
        if print_all:
            #Training data
            N = 5
            for class_index in range(3):
                X.append([[], [], []])
                for i in range(len(self.data)):
                    if self.labels[i] == class_index:
                        X[class_index][0].append(self.data[i][0])
                        X[class_index][1].append(self.data[i][1])
                        X[class_index][2].append(sum(self.data[i][2:]))
        #Test data 
        X.append([[], [], []])
        X.append([[], [], []])
        for i in range(len(predictions)):
            if predictions[i] == test_labels[i]:
                X[N-2][0].append(test_data[i][0])
                X[N-2][1].append(test_data[i][1])
                X[N-2][2].append(sum(test_data[i][2:]))
            else:
                X[N-1][0].append(test_data[i][0])
                X[N-1][1].append(test_data[i][1])
                X[N-1][2].append(sum(test_data[i][2:]))
               
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        #index correspond to the label or to correct/wrong data
        for index in range(N):
            ax.scatter(X[index][0], X[index][1], X[index][2], c=colours[index])
        plt.show()
    
        
    
        
        