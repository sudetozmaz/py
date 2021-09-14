def count_substring(string, sub_string):
    a, l, r = 0, 0, len(sub_string)

    while r <= len(string):
        if string[l:r] == sub_string:
            a += 1
            l += 1
            r += 1
        else:
            l += 1
            r += 1

    return a


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)