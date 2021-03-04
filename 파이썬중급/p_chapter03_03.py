# chapter03_03


# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type으로 확인가능 -> value 

# 일반적인 튜플
pt1 = (1.0,5.0)
pt2 = (2.5,1.5)

from math import sqrt
l_leng1 = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print("1. ")
print(l_leng1)
print()

# 네임드 튜플(튜플인데 딕셔너리 성질을 가지고 있음)
from collections import  namedtuple
Point = namedtuple("Point","x y")
pt3 = Point(1.0, 5.0) # 클래스 형식으로 튜플을 추상화함, 키가 x ,y  value 가 1.0, 5.0 , 인덱스로도 접근은 가능함
pt4 = Point(2.5, 1.5)
print("2. ")
print(pt3)
print(pt4) # 튜풀형태로 데이터가 어떻게 들어있는지 확인가능

l_leng2 = sqrt((pt3.x-pt4.x)**2 + (pt3.y-pt4.y)**2)
print(l_leng2)

# 네임트튜플 선언 방법
Point1 = namedtuple('Point', ["x","y"])
Point2 = namedtuple("Point", 'x y')
Point3 = namedtuple("Point", 'x,y')
Point4 = namedtuple("Point","x y x class",rename=True) # Default = False

# 튜플을 사용하는데 클래스로 나옴
print()
print("3. ")
print(Point1, Point2, Point3, Point4)

# Dict to unpacking
temp_dict = {"x":75,"y":55}


# 객체 생성
p1 = Point1(10,35)
p2 = Point2(20,40)
p3 = Point3(45,20)
p4 = Point4(10,20,30,40)
p5 = Point3(**temp_dict) # 튜플은 언패킹 할떄 *한개 딕셔너리는 **두개


print()
print("4. ")
print(p1)
print(p2)
print(p3)
# rename test
print(p4)
print(p5)
print()

# 사용
print(p1[0],p2[1])
print(p1.x+p2.y) # 이런식으로 쓰는게 더 직관적임
print()

# unpacking
print("5. ")
x,y = p3
print(x,y)

# 네임드 튜플 메소드
print()
print("6.")
temp = [52,38]
# 리스트를 네임드튜플로 변환
# ._make() :  새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields :  필드 네임 확인
print()
print("7. ")
print(p1._fields, p2._fields, p3._fields, p4._fields)

# ._asdict() : OrderDict 반환
print()
print("8. ")
print(p1._asdict)
print(p4._asdict)

# 실 사용 실습
# 반에 20 명있음 4개의 반(A,B,C,D)이 있음
Classes = namedtuple('Classes',["rank","number"])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()
print()
print("9. ")
print(numbers)
print(ranks)

# list comprehension
students =[Classes(rank,number) for rank in ranks for number in numbers]
print()
print("10. ")
print(students)
print(len(students))

# 추천
students2 = [Classes(rank,number) 
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)]]
print()
print("11. ")
print(students2)
# print(students2[0].rank)
print(len(students2))


# 출력
print()
print("12. ")
for s in students2:
    # print(s.rank,s.number)
    print(s)

