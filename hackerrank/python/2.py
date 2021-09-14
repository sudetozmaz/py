import numpy as np

if __name__ == "__main__":
    n, m = (int(i) for i in input().split())

    array = np.array([i.split() for i in (input() for _ in range(n))]).astype(np.float)

    print(np.mean(array, axis=1))
    print(np.var(array, axis=0))
    print(round(np.std(array, axis=None), 11))
