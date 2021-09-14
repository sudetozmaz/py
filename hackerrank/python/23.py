# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def main():
    
    total_sum = 0
    
    number_of_shoes = int(input())
    shoes_sizes_availability = dict(Counter([int(i) for i in input().split()]).items())

    for i in range(int(input())):
        
        cur = [int(i) for i in input().split()]        

        if cur[0] in shoes_sizes_availability:

            if shoes_sizes_availability[cur[0]] > 0:
                total_sum += cur[1]
                shoes_sizes_availability[cur[0]] -= 1
                
    return total_sum
        
    
if __name__=="__main__":
    print(main())