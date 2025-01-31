import pytest
import numpy as np
from src.task15_1 import KMeans

# Test data
data = [
    [15, 39], [15, 81], [16, 6], [16, 77], [17, 40],
    [18, 6], [18, 94], [19, 3], [19, 72], [20, 44]
]

def test_centroids_initialization():
    kmeans = KMeans(k=3)
    kmeans.fit(data)
    assert len(kmeans.centroids) == 3, "Centroids count should match k"

def test_cluster_labels():
    kmeans = KMeans(k=3)
    kmeans.fit(data)
    assert len(kmeans.labels) == len(data), "Each data point should have a cluster label"

def test_predict_function():
    kmeans = KMeans(k=3)
    kmeans.fit(data)
    prediction = kmeans.predict([15, 39])
    assert prediction in [0, 1, 2], "Prediction should return a valid cluster index"



def test_convergence():
    # Use the same initial centroids for consistency
    initial_centroids = [[15, 39], [15, 81], [16, 6]]

    kmeans = KMeans(k=3, max_iters=10)

    # First fit with fixed initial centroids
    kmeans.fit(data, initial_centroids=initial_centroids)
    first_fit_centroids = kmeans.centroids

    # Second fit with the same fixed initial centroids
    kmeans.fit(data, initial_centroids=initial_centroids)
    second_fit_centroids = kmeans.centroids

    assert np.allclose(first_fit_centroids, second_fit_centroids, atol=1e-4), \
        "Centroids should remain stable after sufficient iterations"




if __name__ == "__main__":
    pytest.main()
