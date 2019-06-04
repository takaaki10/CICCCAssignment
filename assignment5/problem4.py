'''
- Each student is represented by the following properties:
o firstName
o lastName
o address
o Year of birth
o Average
Write a function which receives a list of students as its input parameter and
return the student who has the highest average.

 - 各生徒は以下のプロパティで表されます。
o firstName
o lastName
o住所
o生年月日
o平均
入力パラメータとして生徒のリストを受け取る関数を書き、
最も高い平均を持つ生徒を返します。
'''

def findTheHighest(students):
    A,B,C = students
    stuave = (A['Average'],B['Average'],C['Average']) # the list of the students average
    for i in range(len(stuave)):
        if max(stuave) == stuave[i]:
            print(students[i])
            return students[i]




def main():
    stu1 = {'First Name':'A', 'Last Name':'Student', 'Address':'#0101 816 Granville St', 'Year Of Birth':'2000', 'Average': 77}
    stu2 = {'First Name':'B', 'Last Name':'Student', 'Address':'#0201 816 Granville St', 'Year Of Birth':'2004', 'Average': 44}
    stu3 = {'First Name':'C', 'Last Name':'Student', 'Address':'#0301 816 Granville St', 'Year Of Birth':'2013', 'Average': 90}
    findTheHighest((stu1,stu2,stu3))


main()