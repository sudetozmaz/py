def capitalizeWords(arr):
    if len(arr) == 0:
        return []
    else:
        return [arr[0].upper()] + capitalizeWords(arr[1:])


print(capitalizeWords(['foo', 'bar', 'world', 'hello']))
