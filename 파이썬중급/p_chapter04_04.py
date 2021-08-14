# Chapter04_04
# 시퀀스형
# 해시테이블(hash table) -> 적은 리소스로 많은 데이터를 효율적으로 관리하기 위한 데이터 자료구조
# dict -> key 중복 허용 x , Set -> 중복 허용 x
# Dict 및 Set 심화

# imutable Dict

from types import MappingProxyType

d = {'key1':'value1'}

# 수정못하게 읽기전용으로 막기
# Read Only
d_frozen = MappingProxyType(d) # d_frozen은 수정이 불가능 하다

print(d,id(d))
print(d_frozen,id(d_frozen))

# 수정불가
# d_frozen['key2'] = 'value2' # 오류뜸 , 수정이 불가능한 상태이기떄문

# 수정가능
d['key2'] = 'value2'
print(d)

print()
print()

s1 = {'Apple','Orange','Apple','Orange','Kiwi'}
s2 = set(['Apple','Orange','Apple','Orange','Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset(s1) # 읽기만 가능한 프로즌타입임

s1.add('Melon')
print(s1)

# 추가 불가(프로즌타입임)
# s5.add('Melon')
# print(s5)

print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))
print(s5,type(s5))


# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis
print('-'*20)
print(dis('{10}'))
print('-'*20)
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)
from unicodedata import name
print('-'*20)
print({name(chr(i),'') for i in range(0,256)}) # 키보드의 자판을 가져온것



