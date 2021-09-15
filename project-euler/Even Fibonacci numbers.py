### Recursive Solution:
n = int(input())

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci()

### First Solution:
# x = 1
# y = 2
# z = 3
#
# even_sum = 0
#
# while z <= 4000000:
#     z = (x + y)
#
#     x, y = y, z
#
#     if z % 2 == 0:
#         even_sum += z
#
# print(even_sum + 2)

### Better Solution:
# x, y = 1, 2
#
# even_sum = 0
#
# while x <= 4000000:
#     x, y = y, x + y
#
#     if x % 2 == 0:
#         even_sum += x
#
# print(even_sum)
