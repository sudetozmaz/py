largest = 1

for i in range(999):
    for j in range(999):
        num = str(i * j)
        if num == num[::-1] and int(num) > largest:
            largest = int(num)

print(largest)
