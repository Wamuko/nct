import numpy as np

ls = [
    [1, 2, 3],
    [2, 3, 4],
    ]

f = np.vectorize(lambda x: x+1)
ls = f(ls)
print(ls)
