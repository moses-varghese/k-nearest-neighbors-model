"""Compute the predicted value for a given query based on the data provided by knn_regression."""

import numpy as np
import pandas as pd

def knn_regression(n_neighbors, data, query):
    """ The algorithm returns the predicted value for query, a single numeric value, 
        or raises an appropriate exception (such as ValueError) when inappropriate inputs are passed. The functions takes 3 parameters:
        (1)  Parameter k, or n_neighbors
        (2)  data: 2-dimensional numpy array of shape (m, n+1). m denotes the number of samples 
             and n is the number of variables in each sample. +1 is for the labels in each sample.
        (3)  query: 1 dimensional numpy array of shape (1,n).
    """
    m = len(data)
    n = len(data[0])-1
    o = 0
    dis = []
    label = []
    distance = []

    if (n_neighbors == 0):
        raise ValueError("the number of nearest neighbors cannot be zero")
    else:
        pass

    if (n_neighbors > m):
        raise ValueError("the number of nearest neighbors should be less than or equal to the sample size of the data")
    else:
        pass
                            
    if (n_neighbors < 0):
        raise ValueError("the number of nearest neighbors cannot be negative")
    else:
        pass

    if (type(data) != list):
        raise TypeError("data type is not list or array type")
    else:
        pass

    if (data == [[]]):
        raise TypeError("knn_regression() missing 1 required positional argument: 'data'")
    else:
        pass

    if (query == []):
        raise TypeError("knn_regression() missing 1 required positional argument: 'query'")
    else:
        pass

    if (n_neighbors == []):
        raise TypeError("knn_regression() missing 1 required positional argument: 'n_neighbors'")
    else:
        pass

    if (data == [] and n_neighbors == [[]] and query == []):
        raise TypeError("knn_regression() missing 3 required positional arguments: 'n_neighbors', 'data', and 'query'")
    else:
        pass

    for j in range(m):
        di = (((query[o] - data[j][o])**2 + (query[o+1] - data[j][o+1])**2)**(0.5))
        dis.append(di)
        label.append(data[j][n])
        d = {'distance':dis,'value':label}
        df2 = pd.DataFrame(d)
        df1 = df2.sort_values(by='distance')


    for h in range(n_neighbors):
        hy = df1.iloc[h]['value']
        distance.append(hy)
    return(np.mean(distance))
