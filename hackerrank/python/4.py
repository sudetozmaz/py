import warnings

warnings.filterwarnings("ignore")

import numpy as np

if __name__ == "__main__":
    arrayA = np.array([i for i in input().split()]).astype(np.int)
    arrayB = np.array([i for i in input().split()]).astype(np.int)

    print(np.inner(arrayA, arrayB))
    print(np.outer(arrayA, arrayB))
