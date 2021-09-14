import string


def swap_case(s):
    final_str = ""

    for i in range(len(s)):
        if s[i] in string.ascii_lowercase:
            final_str += string.ascii_uppercase[string.ascii_lowercase.index(s[i])]
        elif s[i] in string.ascii_uppercase:
            final_str += string.ascii_lowercase[string.ascii_uppercase.index(s[i])]
        else:
            final_str += s[i]

    return final_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
