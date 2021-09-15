l = [1, 4, 23, 5, 6, 3, 4, 2, 2, 1]


def mul(n):
    if len(n) == 0:
        return 0
    elif len(n) == 1:
        return n[0]
    else:
        return n[len(n) - 1] * mul(n[:len(n) - 1])
        # n[10] = 1            # n[:9] = 2


print(mul(l))
