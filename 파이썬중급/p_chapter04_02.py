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