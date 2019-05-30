"""
Implement a function which receives a list of tuples.
Each tuples represent the transcript of a student with 5 grades between 0 and 100.
Each tuple also contains the name of the student. Example (“Ali”, 67, 87, 90, 45, 39).
The function should return the name and the GPA of the top student.

タプルのリストを受け取る関数を実装します。
各タプルは、0から100までの5段階の学生の成績証明書を表します.
各タプルには、学生の名前も含まれています。 例（「Ali」、67、87、90、45、39）。
この関数は、トップクラスの生徒の名前とGPAを返します。
"""


#grade1: grade of student A
#grade1: grade of student B
#grade1: grade of student C
def GPACalculateAndFindTopScore(grade1, grade2, grade3):
    templist = (grade1, grade2, grade3)

    sumgplist = []
    top = []

    for i in range(len(templist)):
        temp = templist[i]
        gplist = []

        for i in range(len(temp)):
            try:
                int(temp[i])
                if 90 <= temp[i] and temp[i] <= 100:    # 4.0 grade point
                    gplist.append(4.0)

                elif 80 <= temp[i] and temp[i] <= 89:   # 3.0 grade point
                    gplist.append(3.0)

                elif 70 <= temp[i] and temp[i] <= 79:   # 2.0 grade point
                    gplist.append(2.0)

                elif 60 <= temp[i] and temp[i] <= 69:   # 1.0 grade point
                    gplist.append(1.0)

                else:
                    gplist.append(0.0)

            except ValueError:
                name = str(temp[i])

        gpa = round((sum(gplist) / (len(gplist) + 1)), 1)   # round off the second decimal place
        sumgplist.append([gpa, name])

    #print(sumgplist)

    top.append(max(sumgplist)[0])

    print('The top of GPA', '\nName:',max(sumgplist)[1], '\nGPA:' ,max(sumgplist)[0])  # max(sumgplist):  [1.5, 'Mr. A']


def main():
    A = ('Mr. A', 72, 85, 24, 98, 44)   # [2.0, 3.0, 0.0, 4.0, 0.0]  sum of gp 9.0    GPA 1.5
    B = ('Mr. B', 95, 20, 56, 67, 84)   # [4.0, 0.0, 0.0, 1.0, 3.0]  sum of gp 8.0    GPA 1.3333333333333333
    C = ('Mr. C', 87, 65, 64, 69, 61)   # [3.0, 1.0, 1.0, 1.0, 1.0]  sum of gp 7.0    GPA 1.1666666666666667
    GPACalculateAndFindTopScore(A, B, C)

main()


