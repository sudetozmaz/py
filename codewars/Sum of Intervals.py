def sum_of_intervals(intervals):
    f = set()

    for i in intervals:
        for j in range(i[0], i[1]):
            f.add(j)

    return len(f)