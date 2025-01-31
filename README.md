# Sprint 15. Unsupervised Learning - Clustering and Dimensionality Reduction

## Task 1. Customer Segmentation Using K-Means Clustering  

You are tasked with building a Python program that segments customers into clusters based on their annual income and spending score. The objective is to group customers with similar characteristics together using the **K-Means clustering algorithm**.

The dataset consists of 2D data points where:
- The **x-coordinate** represents the **Annual Income** (in $1000s),
- The **y-coordinate** represents the **Spending Score** (a value between 0 and 100).

You need to:
1. **Implement K-Means clustering**: Partition the data points into `k=3` clusters.
2. **Visualize the clusters**: Plot the clusters using `matplotlib`.
3. **Write unit tests**: Validate that the clustering algorithm works correctly using `pytest`.

---

### Input:
A list of 2D points representing customer data:
```python
data = [
    [15, 39], [15, 81], [16, 6], [16, 77], [17, 40],
    [18, 6], [18, 94], [19, 3], [19, 72], [20, 44]
]
```

### Expected Output:
- Correctly cluster the data into `k=3` groups.
- Assign cluster centroids and data point labels.
- Ensure the results are deterministic (fixed initialization for testing).

---

This problem provides hands-on experience with K-Means clustering while encouraging good coding practices through testing and visualization.


## Task 2. Anomaly Detection Using DBSCAN  

You are tasked with building a Python program to identify anomalies in a dataset of 2D points using the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** clustering algorithm. DBSCAN groups points into clusters based on their density and labels sparse, isolated points as **anomalies**.  

The dataset consists of points where most form dense clusters, but a few are scattered anomalies. You need to:  
1. **Implement DBSCAN from scratch**: Identify core points, border points, and noise points.  
2. **Classify points**: Cluster the points and label anomalies.  
3. **Write unit tests**: Ensure the implementation works correctly using `pytest`.  

---

### Input:
A list of 2D points and DBSCAN parameters:  
- `eps`: The maximum distance between points to consider them neighbors.  
- `min_samples`: The minimum number of points required to form a dense region.  

Example input dataset:
```python
data = [
    [1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]
]
eps = 2
min_samples = 2
```

### Expected Output:
- Clusters of dense points.
- Isolated points labeled as anomalies (noise).

Example:
- Cluster 0: \(\{[1, 2], [2, 2], [2, 3]\}\)
- Cluster 1: \(\{[8, 7], [8, 8]\}\)
- Noise: \([25, 80]\)

---

### Hints for Students:
1. **Core, Border, and Noise Points**:
   - **Core Points**: Have at least `min_samples` neighbors.
   - **Border Points**: Within `eps` of a core point but not core themselves.
   - **Noise Points**: Neither core nor border.
2. **Distance Calculation**:
   - Use the Euclidean distance formula:  
     \(\text{distance} = \sqrt{\sum{(x_i - y_i)^2}}\).
3. **Cluster Expansion**:
   - Use a queue to manage points during cluster expansion.
---

### How the Tests Work:
1. **Test for No Clusters**: Ensures all points are labeled as noise when `eps` is very small.
2. **Test for Clusters**: Confirms the correct number of clusters are formed for given `eps` and `min_samples`.
3. **Test for Noise Points**: Checks that the farthest point is labeled as noise.

