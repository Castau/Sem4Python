import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import estimate_bandwidth
from sklearn.cluster import MeanShift
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle


# 1) Get the data on people on the Titanic, their class, sex age, ticket price and whether they survived.
# 2) Load into pandas dataframe
# 3) Drop the PassengerId, Name, Ticket, Cabin columns from the dataframe
# 4) Change sex column into 0 or 1
# 5) One-hot-encode the Embarked column(3 different ports in England)
# 6) Drop rows with missing values
# 7) what is the best bandwidth to use for our dataset? Use sklearn
# 8) Fit data to a meanshift model
# 9) How many clusters do we get
# 10) Add a column to the titanic dataframe with the cluster label for each person
# 11) Get mean values of each cluster group
# 12) Add a column with the size of each cluster group.
# 13) Write out conclusion from the aggregated data.

data = pd.read_csv('train.csv')


def loadAndFixData():
    titanic_data = pd.read_csv('train.csv')

    # Drop useless data
    titanic_data.drop(['PassengerId', 'Name', 'Ticket',
                       'Cabin'], 'columns', inplace=True)
    # Convert gender to binary
    titanic_data['Sex'] = preprocessing.LabelEncoder(
    ).fit_transform(titanic_data['Sex'].astype(str))

    # One-hot encoding
    titanic_data = pd.get_dummies(titanic_data, columns=["Embarked"])

    # Drop rows with missing data
    titanic_data.dropna(inplace=True)
    return titanic_data


def titanicBandwidth(data):
    return estimate_bandwidth(data)


def mNmodel(bandwidth, data):
    model = MeanShift(bandwidth=bandwidth)
    model.fit(data)
    return model


def numOfClusters(model):
    labels = model.labels_
    uniqueLabels = np.unique(labels)
    return len(uniqueLabels)


def addClustersToDataReturnMean(data, model):
    data['cluster_group'] = np.nan
    data_length = len(data)
    for i in range(data_length):
        data.iloc[i, data.columns.get_loc('cluster_group')] = model.labels_[i]
    return data


def groupingByCluster(data):
    clusterData = data.groupby(['cluster_group']).mean()
    clusterData['Counts'] = pd.Series(
        data.groupby(['cluster_group']).size())
    return clusterData


print(loadAndFixData().head())
print(titanicBandwidth(loadAndFixData()))
print(mNmodel(titanicBandwidth(loadAndFixData()), loadAndFixData()))
print(numOfClusters(mNmodel(titanicBandwidth(loadAndFixData()), loadAndFixData())))
print(addClustersToDataReturnMean(loadAndFixData(), mNmodel(
    titanicBandwidth(loadAndFixData()), loadAndFixData())).describe())
print(groupingByCluster(addClustersToDataReturnMean(loadAndFixData(), mNmodel(
    titanicBandwidth(loadAndFixData()), loadAndFixData()))))


# Conclusion
# Cluster 0
# Have 558 passengers
# Survival rate is 33 % (very low) means most of them didn't survive
# They belong to the lower classes 2nd and 3rd class mostly and are mostly male .
# The average fare paid is $15

# Cluster 1
# Have 108 passengers
# Survival rate is 61 % means a little more than half of them survived
# They are mostly from 1st and 2nd class
# The average fare paid is $65

# Cluster 2
# Have 30 passengers
# Survival rate is 73 % means most of them survived
# They are mostly from 1st class
# The average fare paid is $131 (high fare)

# Cluster 3
# Have 15 passengers
# Survival rate is 73 % means most of them survived
# They are mostly from 1st class and are mostly female
# The average fare paid is $239 (which is far higher than the 1st cluster average fare)
# The last cluster has just 3 datapoints so it is not that significant hence we can ignore for data analysis
