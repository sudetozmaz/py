import math

factorize_list = []


def factorize(n):
    count = 0

    while ((n % 2 > 0) == False):
        n >>= 1
        count += 1

    if (count > 0):
        print(2, count)

    for i in range(3, int(math.sqrt(n)) + 1):
        count = 0
        while (n % i == 0):
            count += 1
            n = int(n / i)
        if (count > 0):
            factorize_list.append(i)

        i += 2

    if (n > 2):
        print(n, 1)


factorize(600851475143)
print(max(factorize_list))
