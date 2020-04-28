import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

rawdata = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week11\\balance-scale.data'


def getData(inputdata):
    data = pd.read_csv(inputdata, sep=',', header=None)
    print('Dataset length: ', len(data))
    print('Dataset Shape: ', data.shape)
    return data


# getData(rawdata)

def splitData(inputdata):
    X = inputdata.values[:, 1:5]
    Y = inputdata.values[:, 0]
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=100)
    return X, Y, X_train, X_test, y_train, y_test

# splitData(getData(rawdata))
