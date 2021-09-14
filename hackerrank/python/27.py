from collections import namedtuple

def main():

    N = int(input())
    all_fields = input().split()
    total_sum = 0
    
    for _ in range(N):
        Student = namedtuple("Student", all_fields)
        field1, field2, field3, field4 = input().split()
        the_student = Student(field1, field2, field3, field4)
        total_sum += int(the_student.MARKS)
        
    print(total_sum / N)
        
if __name__ == "__main__":
    main()