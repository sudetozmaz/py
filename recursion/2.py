# Question 1
# Write a recursive function that takes a number and returns the sum of all the numbers from zero to that number.

def sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(-5))
