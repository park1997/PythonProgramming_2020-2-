class Car():
    """
    Car Class
    Author : Park
    Date : 2021.02.15
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든인스턴스가 공유함)
    price_per_raise = 1.0

    def __init__(self,company,details):
        self._company = company
        self._details = details
        # self.car_count =10


    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return "str : {} - {}".format(self._company,self._details)

    # Instance Method 
    # Self : 객체의 고유한 속성값을 이용

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get("price")))

    def get_price(self):
        return "Before Car Price -> Company : {}, price : {}".format(self._company,self._details.get("price"))
    
    def get_price_culc(self):
        return "After Car Price -> Company : {}, price : {}".format(self._company,self._details.get("price")*Car.price_per_raise)

    # classMethod 는 첫번쨰 인자로 cls를 받음
    # cls = Car
    # 클래스 변수를 핸들링 할떄는 클래스 메소드를 반드시 활용하자 !
    @classmethod
    def raise_price(cls,per):
        if per<=1:
            print("Please Enter 1 Or More")
            return 
        cls.price_per_raise=per
        print("Succeed! price incresed!")

    # StaticMethod
    # 클래스로 호출해도되고 인스턴스로 호출해도되는 유연한 함수를 정의할때
    # staticmethod를 사용하자 
    @staticmethod
    def is_bmw(inst):
        if inst._company =="Bmw":
            return "Ok! This car is {}".format(inst._company)
        else:
            return "Sorry This car is not Bmw"

# self 의미
car1 = Car('Ferrari',{'color':'White',"horsepower":400,"price":8000})
car2 = Car('Bmw',{'color':'Black',"horsepower":270,"price":5000})
car3 = Car('Audi',{'color':'Silver',"horsepower":300,"price":6000})

print("1.")
# 전체 정보
car1.detail_info()
car2.detail_info()

print()
print("2. ")
# 가격정보 ( 직접 접근) -> 별로 좋은 방법이 아님 ( 메소드를 통해 접근 해야함)
print(car1._details.get("price"))
print(car2._details["price"])

print()
print("3. ")
# 가격 인상 전
print(car1.get_price())
print(car2.get_price())

print()
print("4. ")
# 가격 인상후
Car.price_per_raise = 1.4
print(car1.get_price_culc())
print(car2.get_price_culc())

print()
print("5. ")
Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())

print()
print("6. ")
# StaticMethod
# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(car3.is_bmw(car3))
# 이런식으로 호출해도됨!!!
# 클래스로 호출
print()
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
print(Car.is_bmw(car3))
