class Car():
    """
    Car Class
    Author : Park
    Date : 2021.02.15
    """

    # 클래스 변수(모든인스턴스가 공유함)
    car_count = 0 

    def __init__(self,company,details):
        self._company = company
        self._details = details
        self.car_count =10
        Car.car_count+=1

    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return "str : {} - {}".format(self._company,self._details)

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get("price")))

    def __del__(self):
        Car.car_count-=1


# self 의미
car1 = Car('Ferrari',{'color':'White',"horsepower":400,"price":8000})
car2 = Car('Bmw',{'color':'Black',"horsepower":270,"price":5000})
car3 = Car('Audi',{'color':'Silver',"horsepower":300,"price":6000})

# id 확인
# 각자 고유의 값을 가지고 있음
print("1.")
print(id(car1))
print(id(car2))
print(id(car3))

print()
print("2. ")

print(car1._company == car2._company)
print(car1 is car2)

print()
print("3. ")
print(dir(car1))
print(dir(car2))

print()
print("4.")
# 딕셔너리 형태로 모든 값을 상세하게 보여줌
print(car1.__dict__)
print(car2.__dict__)

# Doctoring 
# 위에 주석처리 해놓은 상세 설명서를 출력
print(Car.__doc__)

print()
print("5. ")
# 실행
car1.detail_info()
car2.detail_info()

print()
print("6. ")
# 비교
print(car1.__class__)
print(car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__)) # 클래스의 아이디 값이므로 모두 같음
print(car1.__class__ is car2.__class__)
print(car1.__class__ == car2.__class__)

print()
print("7. ")
# 에러
# car1.detail_info() # 이건 에러뜸
Car.detail_info(car1) # 이렇게 하면 에러 안뜸

print()
print("8. ")
# 공유 확인
print(car1.car_count)
print(Car.car_count) # 객체의 수와 같음

print()
print("9. ")
print(dir(car1)) # 이건 클래스 변수가 나옴
print(car1.__dict__) # 이건 클래스 변수가 나오지 않음

print()
print("10. ")
# 객체 삭제
# del 이 될때 __del__ 메소드도 호출이되어 car_count 도 -1 이 됨
del car2
# 삭제 확인
print(Car.car_count)


print()
print("11. ")
# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능( 인스턴스 검색 후 -> 상위(클래스변수, 부모 변수) 에 검색)
# 동일 한 이름의 변수가 생성 되면 변수를 클래스로 호출하는지, 객체를 이용하여 호출하는지에 따라 달라짐
print(car1.car_count)
print(Car.car_count)
