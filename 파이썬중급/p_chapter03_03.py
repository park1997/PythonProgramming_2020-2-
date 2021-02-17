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
pt4 = Point(2.5,1.5)
print("2. ")
print(pt3)
print(pt4) # 튜풀형태로 데이터가 어떻게 들어있는지 확인가능

l_leng2 = sqrt((pt3.x-pt4.x)**2 + (pt3.y-pt4.y)**2)
print(l_leng2)

# 네임트튜플 선언 방법




