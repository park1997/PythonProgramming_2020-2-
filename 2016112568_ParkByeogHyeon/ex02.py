import pandas as pd
class Student:
    def __init__(self,df):
        self.name, self.number, self.department, *datas = datas
        self.math, self.english, self.korean =map(int,datas)

    def show_info(self):
        pass
    def calc_sum(self):
        pass
    def calc_aver(self):
        pass
    def calc_grade(self):
        pass

with open('/박병현/동국대학교/3학년 1학기/파이썬프로그래밍/박병현 파이썬/파이썬프로그래밍01반_CSV.csv') as f :
    df = map(lambda x: x.replace('\n', '').split(','), f.readlines()) #,로 구분 , 공백제거
for i in df:
    print(i)
