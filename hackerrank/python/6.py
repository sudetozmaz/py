import warnings

warnings.filterwarnings("ignore")

import numpy as np

if __name__ == "__main__":
    n = int(input())
    arr = np.array([i for i in (input().split() for _ in range(n))]).astype(np.float)

    print(round(np.linalg.det(arr), 2))
