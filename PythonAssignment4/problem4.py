'''
Design and implement a function which receives two input parameters
1) a list of integer numbers and
2) a number.
The function will find any occurrence of the given input number in the list and remove the number
from the list and finally will return the new list.

2つの入力パラメータを受け取る関数を設計し実装する
1）整数のリスト、および
2）数値を受け取る関数を設計して実装します。
この関数は与えられた入力番号のリスト内の出現箇所を見つけてその番号を削除します
リストから最後に新しいリストを返します。
'''


# numlist: a list of integer numbers
# num: a number to remove from the list
def getListAndNumThenRemoveTheNumFromTheList(numlist, num):
    try:
        print('Remove', num, '\n', numlist, '-> ', end="")
        numlist.remove(num)
        print(numlist, '\n')

    except ValueError:
        print('There is no', num)



def main ():
    #test case1
    print('test case1')
    getListAndNumThenRemoveTheNumFromTheList([3, 0, 7, 1], 7)

    #test case1
    print('test case2')
    getListAndNumThenRemoveTheNumFromTheList([2, 3, 4, 5], 3)

    #test case1
    print('test case3')
    getListAndNumThenRemoveTheNumFromTheList([1, 5, 2, 4], 6)


main()