def exp_sum(num):
    temp = [0] * (num + 1)
    temp[0] = 1

    for i in range(1, num):
        for j in range(i, num + 1):
            temp[j] += temp[j - i]
    return temp[num] + 1
