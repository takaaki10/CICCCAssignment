'''
Define and implement a different version of the linear search function you implemented in Problem 1.
This function is similar to the first one, except this function returns a tuple with two items:
1-The index of the first occurrence and 2-The number of times the number exists in the list.
If the number does not exist in the list, the function will return the tuple constant (-1,0)

問題1で実装した線形検索関数の異なるバージョンを定義して実装します。この関数は最初の関数と似ていますが、
2つの項目を持つタプルが返される点が異なります。 1  - 最初に出現したインデックス、および2  - リスト内にその番号が存在する回数。
番号がリストに存在しない場合、関数はタプル定数（-1,0）を返します。

'''

# intlist: a list of integers
# numtosearch: a number to search for
def linearSearch(intlist, numtosearch):
    times = 0
    for i in range(len(intlist)):
        if intlist[i] == numtosearch:
            times = times + 1

    if times > 0:
        return (intlist.index(numtosearch), times)   # return the index of the number and times of the number

    else:
        return (-1, 0)  # return the tuple constant


def main():
    print('test case1',linearSearch([3, 4, 1, 7, 2, 4, 9, 8, 1], 4))     # test case1 there is two 4
    print('test case2',linearSearch([0, 4, 8, 1, 2, 1, 4, 1, 1], 1))     # test case2 there is four 1
    print('test case3',linearSearch([6, 2, 4, 8, 3, 9, 2, 4, 7], 5))     # test case3 there is no 5


main()
