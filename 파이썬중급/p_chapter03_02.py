# chapter03_02

# 클래스 예제 2
# 벡터(x,y) => 벡터는 크기와 방향을 가짐

class Vector():
    def __init__(self,*arg):
        """
        Create Vector , Example : v = Vector(5,10)
        """
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg

    def __repr__(self):
        ''' 
        Return the vector information
        '''
        return "Vector({} , {})".format(self._x, self._y)

    def __add__(self,other):
        '''
        Return the vector addtion of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self,other):
        return Vector(self._x * other, self._y*other)

    def __bool__(self):
        return bool(max(self._x,self._y))

print("1. ")
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)



# Vevtor 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직메소드 출력

print()
print("2. ")
print(v1,v2,v3)

print()
print("3. ")
print(v1*3)
print(v2*10)
print(bool(v1),bool(v2))
print(bool(v3))





