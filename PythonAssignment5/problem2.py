'''
Write a function which receives a list of integer which may contains repeated numbers.
The function remove the repeated numbers and keeps the distinct number.
The function should return the list of distinct numbers.

繰り返し数を含むかもしれない整数のリストを受け取る関数を書きなさい。
この関数は繰り返しの数を取り除き、異なる数を保持します。
この関数は固有の数のリストを返すべきです。
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
        if cntlist[k] == 1:
            anslist.append(intnums[k])

    print(anslist)
    return anslist


def main():
    test1 = [1, 2, 5, 2, 1] # this answer is 5
    test2 = [8, 4, 0, 4, 2, 8,] # this answer is 0 and 2
    test3 = [8, 1, 3, 1, 9, 3, 6] # this answer is 8, 6 and 9
    print('test case1')
    findRepeatedNumbers(test1)
    print('\ntest case2')
    findRepeatedNumbers(test2)
    print('\ntest case1')
    findRepeatedNumbers(test3)

main()