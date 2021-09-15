def longest_slide_down(pyramid):
    for i in range(len(pyramid) - 1, -1, -1):
        for j in range(i):
            pyramid[i - 1][j] += max(pyramid[i][j], pyramid[i][j + 1])

    return (pyramid[0][0])
