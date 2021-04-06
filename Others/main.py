#samet sarıal 64170037 COE 

word = "ita"
WORDS = list(word)
substrings = [""]


def recursiveGen(word, WORDS, substrings):

    for i in range(0, len(word)):
        for j in range(i, len(word)):
            theWord = (word[i:j+1])
            substrings.append(theWord)

            if theWord[::-1] not in substrings:
                substrings.append(theWord[::-1])

    lastList = substrings



recursiveGen(word, WORDS, substrings)
print(substrings,end=" ")