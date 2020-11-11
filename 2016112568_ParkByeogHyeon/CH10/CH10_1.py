import pandas as pd
class Student:
    def __init__(self,informa):
        self.name, self.number, self.department, self.math, self.english, self.korean=informa
    def show_info(self):
        return "{}\t{}\t{}".format(self.name,self.number,self.department)

    def calc_sum(self):
        return float(self.math)+float(self.english)+float(self.korean)

    def calc_aver(self):
        return self.calc_sum()/3

    def calc_grade(self,m_index,e_index,k_index):
        math_index=m_index
        english_index=e_index
        korean_index=k_index
        student_num=len(students)
        grade_a_num=student_num- int(student_num*0.3)
        grade_b_num=student_num- int(student_num*0.7)
        grade=[]
        if math_index+1>grade_a_num:
            grade.append("A")
        elif math_index+1>grade_b_num:
            grade.append("B")
        else:
            grade.append("C")
        if english_index+1>grade_a_num:
            grade.append("A")
        elif english_index+1>grade_b_num:
            grade.append("B")
        else:
            grade.append("C")
        if korean_index+1>=grade_a_num:
            grade.append("A")
        elif korean_index+1>=grade_b_num:
            grade.append("B")
        else:
            grade.append("C")
        return grade
df = pd.read_csv("파이썬프로그래밍02반_CSV.csv",encoding='CP949')
students=[]
for i in range(len(df.index)):
    a=list(map(str,str(df.iloc[[i]]).split()))
    del a[0:7]
    students.append(Student(a))
result=sorted(students,key=lambda x :x.calc_sum(),reverse=True)
print("{:6}\t{:8}\t{:14}\t{:15}\t{:7}\t\t{:8}".format("No","이름","학번","학과","총점","평균"))
for i,j in enumerate(result):
    print("{}\t{:8}\t{:14}\t\t{:15}\t{:7}\t\t{:2}".format(i+1,j.name,j.number,j.department,int(j.calc_sum()),round(j.calc_aver(),1)))
print()
print()
result_2=sorted(students,key=lambda y: y.name)
math_scores=[int(i.math) for i in result_2]
english_scores=[int(i.english) for i in result_2]
korean_scores=[int(i.korean) for i in result_2]
print(math_scores)
print(sorted(english_scores))
print(korean_scores)
print("{:6}\t{:8}\t{:8}\t{:4}\t{:4}\t{:4}".format("No","이름","학번","수학","영어","국어"))
for i,j in enumerate(result_2):
    real_grade=j.calc_grade(sorted(math_scores).index(int(j.math)),sorted(english_scores).index(int(j.english)),sorted(korean_scores).index(int(j.korean)))
    print('{:4}\t{:8}\t{:12}\t{:4}\t{:4}\t{:4}'.format(i+1,j.name, j.number,real_grade[0],real_grade[1],real_grade[2]))
