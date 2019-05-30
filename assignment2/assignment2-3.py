

num = 0
A = 2
B = 0
list = []

num = input('Enter a number: ')
while (A >= 1):
    num = int(num)
    A = (num / 2)
    B = (num % 2)
    list.insert(0, B)
    num = A

for ans in list:
    print(ans, end="")


"""
num = input('Enter a number: ')
F = (num % 1)


if isinstance(F, float):
    list.append (int(num))
    list.append ('.')
    num = float(num)

    for ans in range(10):
        A = float(num * 2)
        B = int(A)
        list.append (B)
        num = (A % 1)

    for ans in list:
        print(ans, end="")

    print ('...')



else:
    while (A >= 1):
        num = int(num)
        A = (num / 2)
        B = (num % 2)
        list.insert(0, B)
        num = A

    for ans in list:
        print(ans, end="")
"""