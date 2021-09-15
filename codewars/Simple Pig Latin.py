def pig_it(t):
    return " ".join([f"{i[1:]}{i[0]}ay" if i.isalpha() else i for i in t.split()])
