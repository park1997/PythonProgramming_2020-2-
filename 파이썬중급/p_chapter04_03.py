# chapter04_03
# 시퀀스형
# 컨테이너(container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 해시테이블
# key 에 value를 저장하는 구조 
# 파이썬 dict 해시테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])
print(hash(t1))
# print(hash(t2)) # 오류발생(튜플과 같은 불변형 타입만 hashing이 가능하다.)
print()


# dict Setdefault예제
source = (('k1','val1'),('k1','val2'),('k2','val3'),('k2','val4'),('k2','val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)
print()

# Use Setdefault
for k, v in source:
    # default로 k를 넣고 나머지는 리스트에 넣을거야 
    new_dict2.setdefault(k,[]).append(v)
print(new_dict2)
print()

# 주의
new_dict3 = {k:v for k,v in source}
print(new_dict3)

