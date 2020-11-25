import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

#Read the excel
data = pd.read_excel('data.xlsx');
print(data)
print(" ")

#Plot the data as per longitude and latitude
plt.scatter(data['Longitude'], data['Latitude'])
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

#Split the columns and return the required

x = data.iloc[:, 1:3]
print(x)
print(" ")

kmeans = KMeans(2) # No of clusters 2
kmeans.fit(x) #kmeans applied clusters created

identifiedClusters = kmeans.fit_predict(x)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identifiedClusters
print(data_with_clusters)
print(" ")

#Plot the data as per longitude and latitude
plt.scatter(data['Longitude'], data['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()


# Now I want to add language along with latitude longitude clustering
#Assign each language as a value -> Enlish -> 1 French -> 2 Germany -> 3
data_mapped = data.copy()
data_mapped['Language'] = data_mapped['Language']\
    .map({'English' : 1, 'Germany' : 3, 'French' : 2})
print(data_mapped)
print(" ")

x = data_mapped.iloc[:, 3:4]

kmeans = KMeans(3) # No of clusters 2
kmeans.fit(x) #kmeans applied clusters created

identifiedClusters = kmeans.fit_predict(x)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identifiedClusters
print(data_with_clusters)
print(" ")

#Plot the data as per longitude and latitude
plt.scatter(data['Longitude'], data['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

#minimize the distance between points of clusters
#use WCSS for it.
#This will help us find the K -> elbow method
wcss = []
for i in range(1,7):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print(" WCSS ")
print(wcss)


numberCluster = range(1,7)
plt.plot(numberCluster, wcss)
plt.title('The Elbow Method')
plt.xlabel("Number of clusters")
plt.ylabel('Within-cluster sum of square')
plt.show()
