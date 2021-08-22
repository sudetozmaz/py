def maxRepeating(str):
    length = len(str)
    count = 0
    result = str[0]
    index = 1

    for i in range(length):

        current_count = 1
        for x in range(i + 1, length):

            if (str[i] != str[x]):
                break
            current_count += 1

        if current_count > count:
            count = current_count
            result = str[i]
            index = i

    print("Longest same number sequence is of number {} by being repeated {} times in a row, with the first index starting at {}".format(result, count, index))


# Sir, I have also added a counter of the most frequent consecutive number, in advance. Was not not crucial, or asked by you, but done anyways, so please do not get confused.

inputString = str(input("Please enter the string: "))

maxRepeating(inputString)

# https://github.com/vusalismayilovx
