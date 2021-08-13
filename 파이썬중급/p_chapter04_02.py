# chapter04_02
# 시퀀스형
# 컨테이너(container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

print(divmod(100,9))
print(*divmod(100,9))
print(divmod(*(100,9)))

print()

x, y, *rest = range(10)
print(x,y,rest)

x,y,*rest = 1,2,3,4,5,6
print(x,y,rest)

# Mutable(가변) vs Immutable(가변)

l = (15,20,25)
m = [15,20,25]

print(l,id(l))
print(m,id(m))

print()
l*=2    # 튜플은 아이디 값이 바뀜
m*=2    # 리스트는 아이디 값이 안바뀜

print(l,id(l)) 
print(m,id(m))

print()
print()

# sort vs sorted
# reverse, key = len, key = str.Lower, key=func

# sorted : 정렬 후 새로운 객체 반환
f_list =['orange','apple','papaya','lemon','strawberry','coconut']
print('sorted - ',sorted(f_list))
print('sorted(reverse) - ',sorted(f_list,reverse=True))
print('sorted(len) - ',sorted(f_list,key=len))
print('sorted(lambda) - ',sorted(f_list,key=lambda x:x[-1]))    # 끝 글자 기준 정렬
print('sorted(lambda) - ',sorted(f_list,key=lambda x:x[-1],reverse=True))
print()

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인(None)
print('sort - ',f_list.sort(),f_list)
print('sort(reverse) - ',f_list.sort(reverse=True),f_list)
print('sort(len) - ',f_list.sort(key=len),f_list)
print('sort(lambda) - ',f_list.sort(key=lambda x:x[-1]),f_list)
print('sort(lambda) - ',f_list.sort(key=lambda x:x[-1],reverse=True),f_list)
print()

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)
