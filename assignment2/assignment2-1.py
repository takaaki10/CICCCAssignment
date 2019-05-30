


num = 0
ans = 0

while (ans == 0):
    num = int(input('Enter a integer number: '))
    if not (num % 10 == 0):
        ans = (str(num))
        print (ans[::-1])
    else:
        print ('You can enter only the number that can not be divided by 10.')