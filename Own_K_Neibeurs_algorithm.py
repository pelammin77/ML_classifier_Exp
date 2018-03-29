
"""
file: Own_K_neibeurs_algorithm.py
author: Petri Lamminaho
My own K Neighbors algo
Makes random dataset
Predict/vote witch group new point belong
Draw the graph
"""





import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use("fivethirtyeight")

data = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}

new_point  = [5, 3]


def calculate_k_neatrest_neighbors(data, predict, k = 5):
    if len(data)>=k:
        warnings.warn("K on liian pieni luku")


    dist =[]
    for group in data:
        for features in data[group]:
            e_distance = np.linalg.norm(np.array(features) - np.array(predict))
            dist.append([e_distance,group])
    votes =[i[1] for i in sorted(dist)[:k]]
    print(Counter(votes).most_common(1))
    result = Counter(votes).most_common(1)[0][0]
    return result

result = calculate_k_neatrest_neighbors(data, new_point, k =5)
print(result)
for i in data:
    for ii in data[i]:
        plt.scatter(ii[0], ii[1], s = 100, color=i)

plt.scatter(new_point[0], new_point[1], s=100, color=result)
plt.show()
