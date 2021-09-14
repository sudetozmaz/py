import numpy

import warnings

warnings.filterwarnings("ignore")

import numpy as np

if __name__ == "__main__":
    n = int(input())

    arrayA = np.array([i.split() for i in (input() for _ in range(n))]).astype(np.int)
    arrayB = np.array([i.split() for i in (input() for _ in range(n))]).astype(np.int)

    print(np.dot(arrayA, arrayB))
