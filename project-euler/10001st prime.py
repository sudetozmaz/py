def is_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


iter = 5
x = 12

while iter <= 10000:
    if is_prime(x):
        iter += 1

    x += 1

print(x - 1)
