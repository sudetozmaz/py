import warnings

warnings.filterwarnings("ignore")

import numpy as np

if __name__ == "__main__":
    arrayA = np.array([i for i in input().split()]).astype(np.float)
    x = int(input())

    print(np.polyval(arrayA, x))
