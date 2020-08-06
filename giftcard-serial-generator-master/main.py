import random

def codeGenerator(length_of_code_you_want = 8, fstring = '', numcount = 5):
    position_to_keep_constant_1 = 2  # first position to keep constant is position 3, index 2
    position_to_keep_constant_2 = 6  # 2nd position to keep constant is position 7, index 6

    constant_1 = "J"  # the value of the constant at position 3
    constant_2 = "L"  # the value of the constant at position 7

    for num in range(length_of_code_you_want):
        if random.randint(0, 1) == 1:
            x = random.randint(1, 8)
            x += 96
            fstring += (chr(x).upper())
        elif not numcount == 0:
            x = random.randint(0, 9)
            fstring += str(x)
            numcount -= 1

    list_out = list(fstring)
    list_out[position_to_keep_constant_1] = str(constant_1)
    list_out[position_to_keep_constant_2] = str(constant_2)
    string_out = "".join(list_out)
    print(string_out)

for _ in range(3):
    codeGenerator(length_of_code_you_want = 8, fstring = '', numcount = 5)