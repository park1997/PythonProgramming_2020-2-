# chapter04_01
# 시퀀스형
# 컨테이너(container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array, memoryview, deque)
# 불변(tuple, str, bytes)

# a = [3, 3.0, "3"]
# print(a)


# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!'
# chars[2]='h' # 이거 안됨
code_list1 = []

for s in chars:
    code_list1.append(ord(s))
print("1.")
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print()
print("2. ")
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s)>40]
print()
print("3. ")
print(code_list3)

# filter와 map 이용
code_list4 = list(filter(lambda x : x>40, map(ord,chars)))
print()
print("4.")
print(code_list4)

print()
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])


# Generater 생성
import array

# Generater : 한번에 한 개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array("I",(ord(s) for s in chars))
print(array_g)
print(array_g.tolist())
print()

print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))


# 제너레이터 예제
print(('%s'% c+str(n) for c in ['A','B','C','D'] for n in range(1,21)))

for s in ('%s'% c+str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)
print()
print()
# 리스트 주의
# 깊은 복사 얕은복사
marks1 = [['~']*3 for _ in range(4)]
marks2 =[['~']*3]*4 # 아이디 값 까지 같이 복사됨
print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2) # 이게 왜이렇게 될까요......
# marks1 같은 경우는 id값이 모두 다르게 복사가 된거고
# marks2 같은 경우는 하나의 주소값이 4개가 복사가 된것 이기때문에 이런현상이 나옴

# 증명 
print([id(i) for i in marks1])
print([id(i) for i in marks2])

