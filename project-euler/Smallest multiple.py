# 1^1 * 2^4 * 3^2 * 5^1 * 7^1 * 11^1 * 13^1 * 17^1 * 19^1

from sympy.ntheory import factorint

n = int(input())

required = {}

for i in range(1, n + 1):
    for k, v in factorint(i).items():
        if k in required:
            if required[k] < v:
                required[k] = v
        else:
            required[k] = v

r = 1
for k, v in required.items():
    r *= (k ** v)

print(r)
