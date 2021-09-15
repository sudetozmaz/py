n = int(input())

square_of_the_sum = (sum([i for i in range(n + 1)])) ** 2
sum_of_the_square = sum([i ** 2 for i in range(n + 1)])

print(square_of_the_sum - sum_of_the_square)
