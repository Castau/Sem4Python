
# Exercise meanshift
# 1 ) load 'iris_data.csv' into a dataframe
# 2 ) get unique labels(Species column)
# 3 ) plot with a scatter plot each iris flower sample colored by label(3 different colors)
# 4 ) use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters(HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
# 5 ) print out labels, cluster centers and number of clusters(as returned from the MeanShift function
# 6 ) create a new scatter plot where each flower is colored according to cluster label
# 7 ) add a dot for the cluster centers
# 8 ) Compare the 2 plots(colored by actual labels vs. colored by cluster label)


from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import estimate_bandwidth, MeanShift
from itertools import cycle


data = pd.read_csv('iris_csv.csv')
species = list(set(data['Species']))
data['Species'] = preprocessing.LabelEncoder().fit_transform(
    data['Species'].astype(str))

iris = np.array(data)
data.plot.scatter(x='Sepal length', y='Sepal width',
                  c='Species', colormap='cool')
plt.show()

print(data.head())

bandwidth = estimate_bandwidth(data, quantile=0.2)
analyzer = MeanShift(bandwidth=bandwidth)
analyzer.fit(data)
print(bandwidth)

labels = analyzer.labels_
clusterCenters = analyzer.cluster_centers_
numClusters = len(np.unique(labels))

plt.title(f'Meanshift Clustering\n{numClusters} clusters')
plt.scatter(iris[:, 0], iris[:, 1], c=labels, cmap='cool')
plt.scatter(clusterCenters[:, 0],
            clusterCenters[:, 1], marker='X', color='green', s=100, cmap='cool')
cbar = plt.colorbar()
plt.show()
