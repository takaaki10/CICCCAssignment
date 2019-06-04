'''
Write a function which receives a list of integer.
From each number there are exactly 2 in the list except one number that is repeated only once.
The function should return the number that is repeated only once.

整数のリストを受け取る関数を書きなさい。
各番号から1回だけ繰り返される1つの番号を除いて、リストには正確に2つあります。
関数は一度だけ繰り返される数を返すべきです。
'''


def findRepeatedNumbers(intnums):
    cntlist = []
    anslist = []
    count = 0
    for i in range(len(intnums)):
        for j in range(len(intnums)):
            if intnums[i] == intnums[j]:
                count = count + 1

        cntlist.append(count)
        count = 0

    for k in range(len(cntlist)):
        if cntlist[k] == 2:
            anslist.append(intnums[k])

    print(anslist)
    return anslist


def main():
    test1 = [1, 2, 4, 1, 2, 1] # this answer is 2
    test2 = [8, 4, 0, 4, 8, 5, 0, 0] # this answer is 8 and 4
    test3 = [8, 1, 3, 1, 6, 3, 6, 1, 3] # this answer is 6
    print('test case1')
    findRepeatedNumbers(test1)
    print('\ntest case2')
    findRepeatedNumbers(test2)
    print('\ntest case1')
    findRepeatedNumbers(test3)

main()