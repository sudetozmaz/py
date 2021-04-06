s1 = str(input("Please enter the first string: "))
s2 = str(input("Please enter the second string: "))

inputTwoLength = int(len(s2))


i = 0
y = int(inputTwoLength)

def firstTry():
    guesses = str(s1[i:y])

    if guesses == s2:
        print("Found subset at the index of {} !".format(i))
    else:
        nextTries()

def nextTries():
    global i
    global y

    i = i + 1
    y = y + 1

    guesses = str(s1[i:y])

    if guesses == s2:
        print("Found subset at the index of {} !".format(i))
    else:
        for z in range(len(str(inputTwoLength))):
            nextTries()

firstTry()