'''
Class 와 Object를 이용한 수강생 정보 와 성적 관리
CSV 파일로 이름,학번,학과,수학점수,영어점수,국어점수 가 제공된다.
Student 클래스는 아래와 같이 정의된다.

Class--> Student 수강생정보 및 점수관리 클래스

속성 -->
* name 이름
* number 학번
* department 학과
* math 수학점수
* english 영어점수
* korean 국어점수

메서드 -->
* show_info 학생 정보 출력 (이름,학번,학과)
* calc_sum 세과목 총점
* calc_aver 세과목 평균
* calc_grade(과목)
return 해당 과목의 학점
A : 상위 30%
B : 상위 30% ~ 70%이내
C : 상위 70% ~ 100%이내
(동점일 경우, 상위 Grade로)
'''

class Student:
    def __init__(self, datas) :
        self.name, self.number, self.department, *datas = datas
        self.math, self.english, self.korean = map(int, datas)

    def show_info(self) :
        print('{:8}\t{:12}\t{:12}'.format(self.name, self.number, self.department))

    def calc_sum(self) :
        return self.math + self.english + self.korean

    def calc_aver(self) :
        return self.calc_sum()/3

    def calc_grade(self, math_datas, english_datas, korean_datas) :
        math_datas = sorted(map(int, math_datas), reverse = True)
        english_datas = sorted(map(int, english_datas), reverse = True)
        korean_datas = sorted(map(int, korean_datas), reverse = True)
        student_number = len(math_datas)

        # rank 계산 : 동점일 경우, 상위 Grade로
        rank_math = math_datas.index(self.math)+1
        rank_english = english_datas.index(self.english)+1
        rank_korean = korean_datas.index(self.korean)+1

        # grade 계산
        grade = []
        for rank in [rank_math, rank_english, rank_korean] :
            if rank/student_number<= 0.3 : grade.append('A')
            elif rank/student_number<= 0.7 : grade.append('B')
            else : grade.append('C')
        return grade

'''
1) CSV 파일을 읽어들여서, Student 객체를 생성한다.
'''
# ['이름,학번(ID),소속명,Math,English,Korean\n'...] 를 아래처럼 변경
# [['이름', '학번(ID)', '소속명', 'Math', 'English', 'Korean ']....]
with open('파이썬프로그래밍02반_CSV.csv') as f :
    datas = map(lambda x: x.replace('\n', '').split(','), f.readlines())
    col_name, *student_datas = datas
    students = [Student(s) for s in student_datas]

'''
2) 수강생의 총점 과 평균을 출력한다. (총점의 내림차순)
No 이름 학번 학과 총점 평균
1 xxxxx xxxx zzzz 210 70.0
2 yyyyy yyyy kkkk 200 66.7
'''
students_sorted = sorted(students, key = lambda s: s.calc_sum(), reverse = True)
print('\n{:4}\t{:8}\t{:12}\t{:12}\t\t{:4}\t{:4}'.format('No', '이름', '학번', '학과','총점','평균'))
for i, s in enumerate(students_sorted) :
    print('{:4}\t{:8}\t{:12}\t{:12}\t{:4}\t{:4}'.format(i+1,s.name, s.number, s.department, s.calc_sum(), round(s.calc_aver(), 1)))

'''
3) 각 과목의 학점을 출력한다. (이름의 오름차순)
No 이름 학번 수학 영어 국어
1 xxxxx xxxx A B C
2 yyyyy yyyy B A A
'''
math_datas = [s.math for s in students]
english_datas = [s.english for s in students]
korean_datas = [s.korean for s in students]

students_sorted = sorted(students, key = lambda s: s.name)
print('\n{:4}\t{:4}\t{:4}\t{:4}\t{:4}'.format('No', '이름', '수학', '영어','국어'))
for i, s in enumerate(students_sorted) :
    math, english, korean = s.calc_grade(math_datas, english_datas, korean_datas)
    print('{:4}\t{:4}\t{:4}\t{:4}\t{:4}'.format(i+1, s.name, math, english, korean))
