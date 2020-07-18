""" Use PCA to reduce dimensions """
### Run PCA on the data and reduce the dimensions in pca_num_components dimensions
## Reference: https://datascience.stackexchange.com/a/48752
reduced_data = PCA(n_components=5).fit_transform(data1)
results = pd.DataFrame(reduced_data, columns=['pca1', 'pca2', 'pca3', 'pca4', 'pac5'])
# Scatterplot of PCA 1 and PCA 2
sns.scatterplot(x="pca1", y="pca2", hue=data['cluster'], data=results)
plt.title('K-means Clustering with 2 dimensions')
plt.show()

## Cluster of 10
# Conduct clustering and add a cluster column to the data table
clustering_kmeans2 = KMeans(n_clusters=10)
data['cluster2'] = clustering_kmeans2.fit_predict(data)
# Cluster is recorded as integer which won't run in PCA
data.info()
data['cluster2'] = data['cluster2'].astype(float)


### Run PCA on the data and reduce the dimensions in pca_num_components dimensions
## Reference: https://datascience.stackexchange.com/a/48752
reduced_data = PCA(n_components=10).fit_transform(data)
results = pd.DataFrame(reduced_data,
                       columns=['pca1', 'pca2', 'pca3', 'pca4', 'pca5', 'pca6', 'pca7', 'pca8', 'pca9', 'pca10'])
sns.scatterplot(x="pca4", y="pca5", hue=data['cluster'], data=results)
plt.title('K-means Clustering with 2 dimensions')
plt.show()

