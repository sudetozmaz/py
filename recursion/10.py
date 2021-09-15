def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def any_even(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    return any_even(arr[1:], cb)


print(any_even([1, 2, 3, 5], is_even))
