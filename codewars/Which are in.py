def in_array(array1, array2):
    # your code
    return sorted(list(set(i for i in array1 for j in array2 if i in j)))
