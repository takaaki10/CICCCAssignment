'''
Write a function which let’s the user enter English words (no digit in the words).
The user can keep entering English words as long as the user has not entered the word “exit”.
Once the user enters “exit” the function will return and print the list of all distinct words starts with English alphabets.
Like:
- A: Ali, apple, ...
- B: Bob, book
- ... until Z

ユーザーが英語の単語を入力できるようにする関数を作成します（単語に数字は含まれません）。
ユーザは、単語「exit」を入力していない限り、英語の単語を入力し続けることができます。
ユーザーが「exit」と入力すると、関数は戻って英語のアルファベットで始まるすべての異なる単語のリストを表示します。
好きです：
 -  A：アリ、アップル、...
 -  B：ボブ、本
 -  ... Zまで
'''


def inputWords():
    worddict = dict()
    tempdict = dict()
    getword = ''
    templist = []
    while not getword == 'exit':
            getword = str(input('Enter a word: '))
            if getword == 'exit':
                print(worddict)
                break

            elif getword.isalpha():
                if getword[0].upper() in worddict:
                    tempdict = {getword[0].upper():getword}
                    for k in set(worddict) | set(tempdict):
                        vl = []

                    if k in worddict:
                        vl.append(worddict[k])

                    if k in tempdict and tempdict[k] not in templist:
                        templist.append(tempdict[k])
                    worddict[k] = ','.join(templist)
                    tamplist = []
                    print(worddict)
                    # print(temp)
                    # templist.append(getword)
                    # templist = set(templist)
                    # templist = templist
                    # worddict[getword[0].upper()] = templist
                    # templist = ['']
                    # print(worddict)

                else:
                    worddict[getword[0].upper()] = [getword]

            else:
                print('You can enter only a word.')


def main():
    inputWords()


main()