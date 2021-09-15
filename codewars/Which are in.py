def in_array(array1, array2):
    # your code

    return sorted(i for i in array1 if i in array2)


print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
