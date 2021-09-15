from itertools import product


def get_pins(observed):
    pin_dict = {
        '1': ['1', '2', "4"],
        '2': ['1', '2', "3", '5'],
        '3': ['2', '3', "6"],
        '4': ['1', '4', "5", '7'],
        '5': ['2', '4', "5", '6', '8'],
        '6': ['3', '5', "6", '9'],
        '7': ['4', '7', "8"],
        '8': ['5', '7', "8", '9', '0'],
        '9': ['6', '8', "9"],
        '0': ['0', '8']
    }


    return ([''.join(i) for i in product(*[pin_dict[i] for i in observed])])

print(get_pins("100"))
