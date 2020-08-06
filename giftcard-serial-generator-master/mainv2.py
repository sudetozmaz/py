# 8 Symbol Code Generator
import random
import string

allNumbers = ['0','1','2','3','4','5','6','7','8','9']
allLetters = string.ascii_lowercase
code = []

for i in range(100):
    if random.randint(0, 1) == 1:
        x = random.randint(0,25)
        y = allLetters[x]
        code.append(y)
    else:
        if random.randint(0, 1) == 0:
            a = random.randint(0,9)
            b = allNumbers[a]
            code.append(b)


print(code[:11])