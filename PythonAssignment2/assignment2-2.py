
a = 0
b = 0
A = 0
B = 0
C = 0

a, b = map(int, input('Enter 2 numbers: ').split())

A = a
while (A <= b):
    if (A % 3 == 0 and A % 5 == 0):
        print (A, end=" ")
        A = (A + 1)
    else:
        A = (A + 1)

B = a
print('\n')
while (B <= b):
    if (B % 6 == 0 or B % 7 == 0):
        print (B, end=" ")
        B = (B + 1)
    else:
        B = (B + 1)

C = a
print('\n')
while (C <= b):
    if not (C % 3 == 0):
        print (C, end=" ")
        C = (C + 1)
    else:
        C = (C + 1)