n = int(input())

if n:
    temps = sorted(list(map(int, input().split())))
    f = abs(temps[0])

    for i in temps:
        if abs(i) <= abs(f):
            f = i

    print(f)

else:
    print(0)
