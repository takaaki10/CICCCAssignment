# @param A the first input number
# @param B the second input number


# Function Header: def receiveNumbersAndPrintTasks(A, B)
# Type of output: print

def receiveNumbersAndPrintTasks(A, B):
    task1ans = task1(A, B)
    task2ans = task2(A, B)
    task3ans = task3(A, B)
    print(task1ans, task2ans, task3ans)


# Function Header: def task1(A, B)
# Type of output: return value and print

# print all numbers between A and B (A and B not included), which are divisible to both 3 and 5.
def task1(A, B):
    t1 = 0
    t1 = A + 1
    while t1 < B - 1:
        if (t1 % 3 == 0) and (t1 % 5 == 0):
            print(t1, end=" ")

        t1 = t1 + 1

    print('\n')
    t1 = ''  # reset variable t1
    return t1


# Function Header: def task2(A, B)
# Type of output: Return value and print

# print all numbers between A and B (A included by B not included), which are divisible by either 6 or 7.
def task2(A, B):
    t2 = 0
    t2= A
    while t2 < B - 1:
        if (t2 % 6 == 0) or (t2 % 7 == 0):
            print(t2, end=" ")

        t2 = t2 + 1

    print('\n')
    t2 = ''  # reset variable t2
    return t2


# Function Header: def task3(A, B)
# Type of output: Return value and print

# print all numbers between A and B (A and B both included), which are not divisible by 3.
def task3(A, B):
    t3 = 0
    t3= A
    while t3 < B:
        if not (t3 % 3 == 0):
            print(t3, end=" ")

        t3 = t3 + 1

    t3 = ''  # reset variable t3
    return t3


def main():
    receiveNumbersAndPrintTasks(1, 100)

main()
