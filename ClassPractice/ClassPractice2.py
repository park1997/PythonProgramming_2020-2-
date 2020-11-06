# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Park ByeongHyeon
    Date : 2020 - 11 - 01
    Description : calss, Static, Instance Method
    """

    #클래스 변수(모든 인스턴스가 공유 하고 있음)
    price_per_raise = 1.0


    def __init__(self,company,details): #인스턴스 변수
        self._company=company
        #self.car_count=10  이게 찾아지면 이걸 출력하고 이게 없으면 클래스변수에있나? 하고 클래스변수를 찾아본다
        self._details=details

    def __str__(self):
        return "str : {} - {}".format(self._company,self._details)

    def __repr__(self):
        return "repr : {} - {}".foormat(self._company,self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get("price")))

    #Instance Method
    def get_price(self):
        return "Before Car Price -> Company : {} , Price : {}".format(self._company,self._details.get("price"))

    # Instance Method
    def get_price_culc(self):
        return "After Car Price -> Company : {} , Price : {}".format(self._company,self._details.get("price")*Car.price_per_raise)

    #Class Method
    @classmethod
    def raise_price(cls,per):   #클래스 메소드 니까 cls를 받는다
        cls.price_per_raise
        if per <=1:
            print("Please Enter 1 Or More")
            return
        cls.price_per_raise = per
        print("Suceed! Price Increased. ")

    #Static classmethod
    @staticmethod
    def is_bmw(inst):
        if inst._company=="Bmw":
            return " Ok This car is {}".format(inst._company)
        else:
            return " Ok This car is not Bmw. "

#Self 의 의미
car1=Car("Ferarri",{"color":"White","horsepower":400,"price":8000})
car2=Car("Bmw",{"color":"Black","horsepower":270,"price":5000})

# 전체 정보
car1.detail_info()
car2.detail_info()
print()
#가격 정보 (이렇게 직접 접근하는건 좋지않음)(직접 접근)
print(car1._details.get("price"))
print(car2._details.get("price"))
print()
#가격 정보(인상 전)
print(car1.get_price())
print(car1.get_price())
print()
#가격 인상(클래스 메소드 미사용)(이것도 직접접근이라 그렇게 좋진 않음 -> 클래스를 만들)
Car.price_per_raise=1.4
#거격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()
#클래스 메소드로 가격 인상하기  (이 방법을 권장함)(클래스 메소드 사용)
Car.raise_price(1.86)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()
#static method 출력
print(car1.is_bmw(car1)) #인스턴스로 호출하기
print(car2.is_bmw(car2))
print(Car.is_bmw(car1)) #클래스로 호출 을 해도됨
print(Car.is_bmw(car2))
