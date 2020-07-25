from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Elbow method for subset1 of background variables, PVLIT1 and PVNUM1
sse = []
K = range(1, 10)
for k in K:
    km = KMeans(n_clusters=k, n_init = 25, max_iter = 300, random_state= 0)
    km = km.fit(subset1)
    sse.append(km.inertia_)

plt.figure()
plt.plot(K, sse, 'bx-') # With markers on plot
plt.grid(True)
plt.xlabel('k')
plt.ylabel('Sum of Squared Errors')
plt.title('Figure 3. Elbow Method for Optimal k - BKG, PVLIT1, PVNUM1')
plt.show()

# Elbow method for data of background variables and all PVLIT and PVNUM scores
sse = []
K = range(1, 10)
for k in K:
    km = KMeans(n_clusters=k, n_init = 25, max_iter = 300, random_state= 0)
    km = km.fit(data)
    sse.append(km.inertia_)

plt.figure()
plt.plot(K, sse, 'bx-')
plt.grid(True)
plt.xlabel('k')
plt.ylabel('Sum of Squared Errors')
plt.title('Figure 4. Elbow Method for Optimal k - BKG, PVLIT, PVNUM')
plt.show()