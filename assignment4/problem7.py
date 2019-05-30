'''
Design and implement a function which receives an list of integer and print and return
the mirror of the array. (Assume that the input list is 2D)

整数のリストを受け取り、配列のミラーを出力する関数を設計して実装します。 （入力リストが2Dであると仮定します）

ideal output
[9 8 7 8 9]
[6 5 4 5 6]
[3 2 1 2 3]
[6 5 4 5 6]
[9 8 7 8 9]
'''


# twoDList: 2D list of integer numbers
def mirror2DList(twoDList):
    receive = []
    mirrorlist = []
    for i in range(len(twoDList)):
        oneofthem = twoDList[i]  # take one of three lists
        for j in range(len(twoDList)):
            numofthem = oneofthem[j]    # take one out of multiple numbers
            if j > 0:
                for k in range(len(twoDList) - 2):
                    receive.append(numofthem)
                    receive.insert(0, numofthem)

            else:
                receive.append(numofthem)

        if i > 0:
            mirrorlist.append(receive)
            mirrorlist.insert(0, receive)

        else:
            mirrorlist.append(receive)

        receive = []

    for l in range(len(mirrorlist)):
        print(mirrorlist[l])



def main():
    print('test case1')
    mirror2DList([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    print('\ntest case2')
    mirror2DList([[-9, -8, -7],
                  [-6, -5, -4],
                  [-3, -2, -1]])
    print('\ntest case3')
    mirror2DList([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])


main()