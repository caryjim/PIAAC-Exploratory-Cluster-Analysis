import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import var

""" Visualize the raw data """
plt.figure()
plt.scatter(bkg_lit_num_cleaned.iloc[:, 2], bkg_lit_num_cleaned.iloc[:, 4])
plt.xlabel('Education')
plt.ylabel('Write at Home')
plt.title("Visualization of Education Level and Index of Writing Activity at Home")
plt.show()

plt.figure()
plt.scatter(bkg_lit_num_cleaned['ICTHOME'], bkg_lit_num_cleaned['PVLIT1'])
plt.xlabel('Index of ICT Use at Home')
plt.ylabel('Literacy Plausible Value 1')
plt.title("Visualization of ICT Use at Home and Literacy Scores")
plt.show()

plt.figure()
plt.scatter(bkg_lit_num_cleaned['ICTHOME'], bkg_lit_num_cleaned['PVNUM1'])
plt.xlabel('Index of ICT Use at Home')
plt.ylabel('Literacy Plausible Value 1')
plt.title("Visualization of ICT Use at Home and Numeracy Scores")
plt.show()

plt.figure()
plt.scatter(bkg_lit_num_cleaned['ICTHOME'], bkg_lit_num_cleaned['ICTWORK'])
plt.xlabel('Index of ICT Use at Home')
plt.ylabel('Index of ICT Use at Work')
plt.title("Visualization of ICT Use at Home and ICT Use at Work ")
plt.show()

""" Correlation Plots """
# Correlation of background variables with Pearson R method
correlation = bkg_cleaned.corr(method="pearson")
# Viz of correlation table of background variables
# Color Palettes for Seaborn: https://seaborn.pydata.org/tutorial/color_palettes.html
# Color Maps for Matplotlib: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
sns.heatmap(correlation, vmin=-1, vmax=1, cmap="Spectral", linewidths=0.25)
plt.title("Correlation of Background Variables - Raw Data")
plt.show()

# Correlation on the cleaned background data
correlation_2 = bkg_cleaned.corr(method="pearson")
sns.heatmap(correlation_2, vmin=-1, vmax=1, cmap="Spectral", linewidths=0.25)
plt.title("Figure 1. Correlation of Background Variables without NULL")
plt.show()

# TODO: Add variance and covariance calculations
#  """ Variance and Covariance Matrix """

variance = var(v, ddof=1)
covMatrix = np.cov(bkg_array, bias=True)
# ax = sns.heatmap(correlation, cmap="YlGnBu")
# f,ax = plt.subplots(figsize=(40, 40))
# sns.heatmap(corr_pv, cmap="YlGnBu", linewidths=.5,ax=ax, annot=True)
# plt.show()


"Distribution of Clusters for Background Variables with PVLIT1 and PVNUM1"
data1['cluster'].unique()
data1['cluster'].value_counts()

sns.set(color_codes=True)  # Set SNS plots aesthetic parameters in one step

# Count Plot from Seaborn for Categorical Count Data
sns.countplot(x='cluster', data=data1, color='blue')
plt.title(" Figure 2. Frequency Count of Cases in Each Cluster")
plt.show()

# Categorical Plot groups variables by categories
sns.catplot(x='cluster', col='GENDER_R', data=data1, kind='count')
plt.title(" Distribution of Gender in Clusters, 1 - Male, 2 - Female ")
plt.show()

# Plot of education level by clusters
sns.catplot(x="cluster", col="B_Q01A", data=data1_1, kind="count")
plt.show()

sns.catplot(x="cluster", hue='GENDER_R', col="B_Q01A", data=data1, kind="count")
plt.show()

# Scatter plots of cluster1 variables - PVLIT1, PVNUM1, for each cluster
plt.scatter(data1['PVLIT1'], data1['PVNUM1'], c=data1['cluster'])
plt.colorbar()
plt.title('Distribution of PVLIT1 and PVNUM1 by Clusters')
plt.xlabel('PVLIT1')
plt.ylabel('PVNUM1')
plt.show()

# TODO : Check the Array Histrogram Function
# Array Histrogram needs exploration
a = np.histogram(predicted_km, bins=[0, 1, 2, 3, 4, 5])
plt.hist(a, bins=[0, 1, 2, 3, 4, 5])
plt.title('Distribution of Clusters from Subset Data 1')
plt.show()

# Create Array of Cluster Centers
# subset1 is created from subset1 with cluster number added to the last column
# cluster_labels is a variable to store the cluster information as array
cluster_labels = clustering_kmeans.labels_
# cluster_centers is a variable to store the cluster center information as array
cluster_centers = clustering_kmeans.cluster_centers_
# Columns headings are labels from the dataset
# Rows are the centroids value of each cluster for each variables
plt.plot()
plt.title('k means centroids')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker="x", color='r')
plt.show()

# How to visualized multiple dimension data
# Use PCA to reduce dimensions before plotting see reference below
# Reference: https://datascience.stackexchange.com/a/48752
