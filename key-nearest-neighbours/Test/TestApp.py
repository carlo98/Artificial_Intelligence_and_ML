from kNN.myKNN import myKNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
import numpy as np

choice = "iris"

if __name__ == '__main__':
    
    if choice == "iris":
        #Preparing data IRIS
        iris = datasets.load_iris()
        iris_data = iris.data
        iris_labels = iris.target
        train_data, test_data, train_labels, test_labels = train_test_split(iris_data, iris_labels, test_size=0.33, random_state=np.random.seed(np.random.randint(100)))
    elif choice == "bc":
        #Preparing data BREAST CANCER
        breast_cancer = datasets.load_breast_cancer()
        bc_data = breast_cancer.data
        bc_labels = breast_cancer.target
        train_data, test_data, train_labels, test_labels = train_test_split(bc_data, bc_labels, test_size=0.33, random_state=np.random.seed(np.random.randint(100)))
    #Testing kNN
    predicted_labels = []
    testkNN = myKNN(train_data, train_labels)
    for i in range(len(test_data)):
        neighbours = testkNN.find_neighbours(test_data[i])
        result = testkNN.vote_distance_weight(neighbours)
        print("Predicted: ",result," correct: ",test_labels[i])
        predicted_labels.append(result[0])
    print("Accuracy score: ",accuracy_score(test_labels, predicted_labels))
    
    #Plotting data in 3D
    testkNN.plot(predicted_labels, test_data, test_labels, print_all=True)
    