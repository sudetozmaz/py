from collections import deque

if __name__ == "__main__":

    d = deque()

    n = int(input())

    try:
        for i in range(n):
            inp = input().split()

            if inp[0] != inp[-1]:
                eval(f"d.{inp[0]}({inp[1]})")
            else:
                eval(f"d.{inp[0]}()")
    except:
        print(False)

    print(" ".join([str(i) for i in d]))
