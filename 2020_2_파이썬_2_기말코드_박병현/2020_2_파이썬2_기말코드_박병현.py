# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:48:21 2020

This is code-template of Python Programming Final Exam
"""
##################################################################
# Number 1
# printing student information with formatting % or format function
##################################################################

name = "박병현"
student_ID = 2016112568
department = "산업시스템공학과"

"""

**************************************************
2020년 2학기  파이썬프로그래밍  기말고사 답안지
**************************************************

******************************
이름     :  박병현
학번(ID) :  2016112568
학과     :  산업시스템공학과
******************************

"""
# 수강생 본인 정보로 대체하여 위 포맷과 같이
# 출력하는 프로그램을 코딩하시오
# print()

print("{}".format("*"*50))
print("{}".format("2020년 2학기 파이썬프로그래밍 기말고사 답안지"))
print("{}".format("*"*50))
print()
print("{}".format("*"*40))
print("{}\t\t:\t{}".format("이름",name))
print("{}\t:\t{}".format("학번(ID)",student_ID))
print("{}\t\t:\t{}".format("학과",department))
print("{}".format("*"*40))



##################################################################
# Number 2 (2분반)
# multiple elements in tuple
##################################################################

in_tuple = (1, 2, 5, 4, 3, 2, 9, 4, 7, 8, 9, 9, 3, 7, 3)

## remove multiple elements
result={}
for i in in_tuple:
    if i not in result:
        result[i]=1
    else:
        result[i]+=1
result=sorted(result.items(), key=lambda x:x[1], reverse=True)
max_number=result[0][1]
real=[i[0] for i in result if i[1]==max_number]
out_tuple=tuple(set(in_tuple))
max_num=max(real)
## count multiple elements


## print results
print("입력 : 주어진 튜플 : ", in_tuple)
print("출력 : 중복 제거 튜플 : ", out_tuple)
print("       가장 많은 중복 요소 : ", max_num)


##################################################################
# Number 3
# analysis of korea flaoting population
#
##################################################################

import csv

#참고용 파일 open, read 예시

f = open("korea_floating_population_data.csv", 'r')
reader = csv.reader(f)


##
## 지역별, 주중/주말,  남자/여자, 연령대별 분석 코드
##

jongro_20num,jongro_50num,dobong_20num,dobong_50num,jongro_all,dobong_all=0,0,0,0,0,0
for i in reader:
    if "종로구" in i[7]:
        jongro_20num+=int(i[10])+int(i[15])
        jongro_50num+=int(i[13])+int(i[18])
        jongro_all+=sum(map(int,i[9:]))
    if "도봉구" in i[7]:
        dobong_20num+=int(i[10])+int(i[15])
        dobong_50num+=int(i[13])+int(i[18])
        dobong_all+=sum(map(int,i[9:]))

## 출력 format
print("*"*55)
print("{:<4s}   {:<5s}  {:<4s}    {:<5s}   {:<5s}  {:<8s}".format("조사지역", "전체수 ", "20대", "20대비율", "50대", "50대비율"))
print("{:<8s}   {:<8s}  {:<8s}  {:<8s}   {:<8s} {:<8s}".format("Area", "Total ", "No.", "Rate%", "No.", "Rate%"))
print("*"*55)
print("{:6} {:7}  {:6} {:9}  {:6} {:9}".format("종로구",jongro_all,jongro_20num,round(jongro_20num*100/jongro_all,3),jongro_50num,round(jongro_50num*100/jongro_all,3)))
print("{:6} {:7}  {:6} {:9}  {:6} {:9}".format("도봉구",dobong_all,dobong_20num,round(dobong_20num*100/dobong_all,3),dobong_50num,round(dobong_50num*100/dobong_all,3)))
print("{}".format("-"*55))
## 결과 출력


f.close()
