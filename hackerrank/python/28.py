# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from collections import OrderedDict

def main():
    d = OrderedDict()
  
    for _ in range(int(input())):
        item, space, quantity = input().rpartition(' ')
        d[item] = d.get(item, 0) + int(quantity)
    
    for item, quantity in d.items():
        print(item, quantity)

if __name__ == "__main__":
    main()
