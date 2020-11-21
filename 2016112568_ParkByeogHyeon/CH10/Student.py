import csv

class Student:

    math = []
    eng = []
    kor = []
    count = 0

    def __init__(self, name, num, dept, math, eng, kor):
        self.name = name
        self.num = num
        self.dept = dept
        self.math = math
        self.eng = eng
        self.kor = kor

        Student.math.append(math)
        Student.eng.append(eng)
        Student.kor.append(kor)
        Student.count += 1

    def show_info(self):
        print('{} {} {} {} {} {}'.format(self.name, self.num, self.dept, self.math, self.eng, self.kor))

    def calc_sum(self):
        return self.math + self.eng + self.kor

    def calc_aver(self):
        return (self.math + self.eng + self.kor) / 3

    def calc_grade(self, subject):
        rank = 0
        if subject == 'math':
            for i in Student.math:
                if self.math < i:
                    rank += 1
            rank += 1
            if rank <= Student.count*0.3:
                return 'A'
            elif rank > Student.count*0.3 and rank <= Student.count*0.7:
                return 'B'
            else:
                return 'C'

        elif subject == 'eng':
            for i in Student.eng:
                if self.eng < i:
                    rank += 1
            rank += 1
            if rank <= Student.count*0.3:
                return 'A'
            elif rank > Student.count*0.3 and rank <= Student.count*0.7:
                return 'B'
            else:
                return 'C'

        elif subject == 'kor':
            for i in Student.kor:
                if self.kor < i:
                    rank += 1
            rank += 1
            if rank <= Student.count*0.3:
                return 'A'
            elif rank > Student.count*0.3 and rank <= Student.count*0.7:
                return 'B'
            else:
                return 'C'

student = []
f = open("파이썬프로그래밍02반_CSV.csv", 'r')
rdf = csv.reader(f)
i = 0
for line in rdf:
    if i > 0:
        student.append(Student(line[0], line[1], line[2], int(line[3]), int(line[4]), int(line[5])))
    i+=1

f.close()

student_calc = []
for i in student:
    student_calc.append([i.name, i.num, i.dept, i.calc_sum(), i.calc_aver()])

# print("Student 객체 show_info() 출력 테스트용")
# for i in student:
#     i.show_info()

print("2) 총점순 출력")
student_calc = sorted(student_calc, key=lambda s:s[3], reverse=True)
no = 1
print('{:<3} {:ㅤ<4} {:ㅤ<6} {:ㅤ<13} {:ㅤ<3} {:ㅤ<5}'.format('No','이름','학번','학과','총점','평균'))
for i in student_calc:
    print('{:<3} {:ㅤ<4} {:ㅤ<11} {:ㅤ<13} {:ㅤ<5} {:ㅤ<5.1f}'.format(str(no), i[0], i[1],i[2],i[3],i[4]))
    no+=1

no = 1
student_grade = []
for i in student:
    student_grade.append([i.name, i.num, i.dept, i.calc_grade('math'), i.calc_grade('eng'), i.calc_grade('kor')])
print("3) 이름순 학점 출력")
student_grade = sorted(student_grade, key=lambda s:s[0], reverse=False)
print('{:<3} {:ㅤ<4} {:ㅤ<6} {:ㅤ<13} {:ㅤ<3}   {:ㅤ<3}    {:ㅤ<3}'.format('No','이름','학번','학과','수학','영어','국어'))
for i in student_grade:
    print('{:<3} {:ㅤ<4} {:ㅤ<11} {:ㅤ<13} {:ㅤ<5} {:ㅤ<5} {:ㅤ<5}'.format(str(no), i[0], i[1],i[2],i[3],i[4], i[5]))
    no+=1
