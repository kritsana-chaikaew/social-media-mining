import numpy as np
import matplotlib.pyplot as plt

def nearest(data, means):
    distances = [np.linalg.norm(data-mean) for mean in means]
    return np.argmin(distances)

def clustering(clusters, data, means):
    idx = nearest(data, means)
    clusters[idx] = np.append(clusters[idx], [data], axis=0)

def plot(k, means, clusters):
    plt.figure()
    for i in range(k):
        for d in clusters[i]:
            plt.plot([d[0],means[i][0]], [d[1],means[i][1]], 'bo-')
            plt.plot(means[i][0], means[i][1], 'ro')
    plt.draw()

K = 6
x_means = (np.random.uniform(0, 10, K))
y_means = (np.random.uniform(0, 10, K))
data = np.ndarray(shape=(0, 2))

for i in range(K):
    for j in range(10):
        x = np.random.normal(x_means[i], 1, 1)[0]
        y = np.random.normal(y_means[i], 1, 1)[0]
        data = np.append(data, [[x,y]], axis=0)

for random_try in range(3):
    means = data.copy()
    np.random.shuffle(means)
    means = means[:K]
    old_means = np.ndarray(shape=(0, 2))

    clusters = {}

    iteraion = 0
    max_iteration = 10
    while len(np.where(means!=old_means)[0]) != 0:
        old_means = means.copy()

        for i in range(K):
            clusters[i] = np.ndarray(shape=(0, 2))

        for d in data:
            clustering(clusters, d, means)

        for i in range(K):
            means[i] = [
                    np.average(clusters[i][:, 0]),
                    np.average(clusters[i][:, 1])]

        iteraion += 1
        if iteraion == max_iteration:
            break

    plot(K, means, clusters)
plt.show()
