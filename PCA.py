from time import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

""" Use PCA to reduce dimensions """
""" K-means clustering with PCA """
# Run PCA on the data and reduce the dimensions in pca_num_components dimensions
# Ref: https://365datascience.com/pca-k-means/

""" Standardization of the data"""
scaler = StandardScaler()
data_std = scaler.fit_transform(bkg_lit_num_cleaned)

pca = PCA()
pca.fit(data_std)

# How much variance is explained by each of the components?
pca.explained_variance_ratio_

plt.figure()
plt.plot(pca.explained_variance_ratio_.cumsum(), marker = 'o', linestyle = '--')
plt.grid(True)
plt.title('Explained Variance by Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.show()

# If we use 80% rule to preserve the variance
pca = PCA(n_components= 8)
pca.fit(data_std)
pca.transform(data_std)
scores_pca = pca.transform(data_std)

# K mean clustering with PCA
wcss = []
for i in range (1, 25):
    kmeans_pca = KMeans(n_clusters= i, init= "k-means++", random_state= 42)
    kmeans_pca.fit(scores_pca)
    wcss.append(kmeans_pca.inertia_)

plt.figure()
plt.plot(range(1, 25), wcss, marker='o')
plt.grid()
plt.xlabel("WCSS")
plt.ylabel('K-means with PCA clustering')
plt.show()

kmeans_pca = KMeans(n_clusters=5, init='k-means++', random_state= 42)
kmeans_pca.fit(scores_pca)


### Run PCA on the data and reduce the dimensions in pca_num_components dimensions
## Reference: https://datascience.stackexchange.com/a/48752
reduced_data = PCA(n_components=10).fit_transform(data)
results = pd.DataFrame(reduced_data,
                       columns=['pca1', 'pca2', 'pca3', 'pca4', 'pca5', 'pca6', 'pca7', 'pca8', 'pca9', 'pca10'])
sns.scatterplot(x="pca4", y="pca5", hue=data['cluster'], data=results)
plt.title('K-means Clustering with 2 dimensions')
plt.show()

