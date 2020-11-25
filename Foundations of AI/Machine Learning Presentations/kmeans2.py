import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
from sklearn import preprocessing
# from numpy.linalg import norm
# from matplotlib.image import imread
# from sklearn.datasets.samples_generator import (make_blobs,
#                                                 make_circles,
#                                                 make_moons)
# from sklearn.cluster import KMeans, SpectralClustering
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import silhouette_samples, silhouette_score
# sns.set_context('notebook')
# plt.style.use('fivethirtyeight')
from warnings import filterwarnings
filterwarnings('ignore')


#Read the excel
data = pd.read_excel('kmeans2.xlsx');
print(data)


#Plot the data as per satisfaction and lyalty
plt.scatter(data['Satisfaction'], data['Loyalty'])
plt.xlabel("Satisfaction")
plt.ylabel('Loyalty')
plt.show()

#Brand Loyalty let assum range (-2.5 to 2.5)
x = data.copy()

kmeans = KMeans(2) # No of clusters 2
kmeans.fit(x) #kmeans applied clusters created

identifiedClusters = kmeans.fit_predict(x)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identifiedClusters
print(data_with_clusters)

plt.scatter(data['Satisfaction'], data['Loyalty'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlabel("Satisfaction")
plt.ylabel('Loyalty')
plt.show()

#standarize using simplest method
x_scaled = preprocessing.scale(x)

wcss = []
for i in range(1,7):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print(wcss)

numberCluster = range(1,7)
plt.plot(numberCluster, wcss)
plt.title('The Elbow Method')
plt.xlabel("Number of clusters")
plt.ylabel('Within-cluster sum of square')
plt.show()

kmeans_new = KMeans(3)
kmeans_new.fit(x_scaled) ## the cluster created is based on the standarized data
#but the cluster mapping is done w.r.t to the original data
cluster_new = x.copy()
newClusterCount = kmeans_new.fit_predict(x_scaled)
cluster_new['Cluster_pred'] = newClusterCount
print("cluster_new")
print(cluster_new)

plt.scatter(cluster_new['Satisfaction'], cluster_new['Loyalty'],
            c=cluster_new['Cluster_pred'], cmap='rainbow')
plt.xlabel("Satisfaction")
plt.ylabel('Loyalty')
plt.show()
