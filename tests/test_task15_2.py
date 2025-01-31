import pytest
from src.task15_2 import DBSCAN
data = [
    [1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]
]
eps = 2
min_samples = 2


def test_no_clusters():
    dbscan = DBSCAN(eps=0.1, min_samples=2)
    dbscan.fit(data)
    assert all(label == -1 for label in dbscan.labels), "All points should be noise with small `eps`."


def test_clusters_formed():
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(data)
    assert len(set(dbscan.labels)) - (1 if -1 in dbscan.labels else 0) == 2, "There should be two clusters."


def test_noise_points():
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(data)
    assert -1 in dbscan.labels, "There should be noise points."
    assert dbscan.labels[-1] == -1, "Point [25, 80] should be labeled as noise."


if __name__ == "__main__":
    pytest.main()
