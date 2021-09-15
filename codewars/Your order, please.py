def run_sorted(x):
    return [int(i) for i in x if i.isdigit()][0]


def order(sentence):
    # code here
    return " ".join(sorted(sentence.split(), key=run_sorted))


### Shorter Solution with lambda
# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
