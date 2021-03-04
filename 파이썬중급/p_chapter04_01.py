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
