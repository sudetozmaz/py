# Enter your code here. Read input from STDIN. Print output to STDOUT

import datetime
import calendar


def main(date_str):
    
    
    date_str = str(date_str).split()
    date_str = f"{'-'.join([date_str[0], date_str[1], date_str[-1]])}"
    date_str = datetime.datetime.strptime(date_str, '%m-%d-%Y')

    print(str(calendar.day_name[date_str.weekday()]).upper())
    

if __name__ == "__main__":
    
    main(input())