def summing(n):
    return sum([int(str(n)[i]) ** (i + 1) for i in range(len(str(n)))])

def sum_dig_pow(a, b):
    # your code here
    return [i for i in range(a, b + 1) if i == summing(i)]
