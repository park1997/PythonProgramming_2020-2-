# Chapter_05_01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환(return)

def factorial(n):
    '''
    Factorial Function -> n : int
    '''
    if n ==1:
        return 1
    return n * factorial(n-1)

class A:
    pass
print(factorial(5))
print(factorial.__doc__)
print(type(factorial),type(A))
print(set(sorted(dir(factorial)))-set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial
print(var_func(10))
print(list(map(var_func,range(1,11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
# es6

# 홀수만 factorial이 나옴
print(list(map(var_func, filter(lambda x : x%2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i%2]) 
print()

# reduce
from functools import reduce
from operator import add

print(sum(range(1,11)))
print(reduce(add,range(1,11)))

print()
# 익명함수(Lambda)
# 익명함수를쓸때는 가급격 주석을 달아라
# 가급적 함수를 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t:x+t,range(1,11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인

print(callable(str),callable(A),callable(list),callable(var_func),callable(3.14))
print()

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
# 함수를 인자로 전달 가능하고 함수를 변수에 할당 했음
five = partial(mul,5)
print(five(10))

# 고정 추가
six = partial(five,6)
print(five(10))
print([five(i) for i in range(1,11)])
print(list(map(five,range(1,11))))