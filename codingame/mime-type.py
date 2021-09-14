n = int(input())
q = int(input())

exts = {}

for i in range(n):
    ext, mt = input().split()
    exts[ext.lower()] = mt

for i in range(q):
    fname = input()

    ext_input = fname.split(".")
    if "." in fname and ext_input[-1].lower() in exts:
        print(exts[f"{ext_input[-1].lower()}"])
    else:
        print("UNKNOWN")
