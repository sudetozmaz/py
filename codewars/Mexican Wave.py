def wave(people):
    # Code here
    return [people[:i] + people[i].upper() + people[i + 1:] for i in range(len(people)) if not people[i].isspace()]
