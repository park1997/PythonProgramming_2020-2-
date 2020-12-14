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
department = "산업시스템공학"

"""

**************************************************
2020년 2학기  파이썬프로그래밍  기말고사 답안지
**************************************************

******************************
이름     :  홍길동
학번(ID) :  20201110111
학과     :  융합교육원
******************************

"""
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
# Number 2 (1분반)
# mean_of_n, max_of_n, min_of_n
# n : 3개 이상의 정수로 입력됨을 가정
##################################################################

sum=0
def mean_of_n(in_nums):
    global sum
    for i in in_nums:
        sum += i
    result = sum / len(in_nums)
    return result

def max_of_n(in_nums):
    max=in_nums[0]
    for i in in_nums:
        if i>max:
            max=i
    return max

def min_of_n(in_nums):
    min=in_nums[0]
    for i in in_nums:
        if i<min:
            min=i
    return min

in_num_str = input("정수를 여러 개 입력하시오 : ")
in_num_list = list(in_num_str.split())
for i in range(len(in_num_list)):
    in_num_list[i] = int(in_num_list[i])

print("평균값은 ", mean_of_n(in_num_list))
print("최댓값은 ", max_of_n(in_num_list))
print("최솟값은 ", min_of_n(in_num_list))


##################################################################
# Number 3
# analysis of usa alcohol consumption
##################################################################
import csv
f = open("usa_alcohol_comsumption_data.csv", 'r')
reader = csv.reader(f)
a={}
a_num={}
nothing=0
for i in reader:
    nothing+=1
    if nothing==1:
        continue
    if 2000<=float(i[1]) and float(i[1])<=2009:
        if i[0] not in a:
            a[i[0]]=[float(i[2]),float(i[3]),float(i[4])]
        else:
            a[i[0]][0]+=float(i[2])
            a[i[0]][1]+=float(i[3])
            a[i[0]][2]+=float(i[4])
        if i[0] not in a_num:
            a_num[i[0]]=1
        else:
            a_num[i[0]]+=1
for i in a:
    a[i][0]=a[i][0]/a_num[i]
    a[i][1]=a[i][1]/a_num[i]
    a[i][2]=a[i][2]/a_num[i]
a=sorted(a.items(), key= lambda x:x[1][1], reverse=True)
print("sorting by wine >>")
print(f'{"No.":^5}{"State":^20}{"beer":>15}{"wine":>15}{"spirits":>15}')
print("="*70)
for i,j in enumerate(a):
    print("{:4}\t{:20}{:13.2f}{:14.2f}{:15.2f}".format(i,j[0],round(j[1][0],2),round(j[1][1],2),round(j[1][2],2)))
