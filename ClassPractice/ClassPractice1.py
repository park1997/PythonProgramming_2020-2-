# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리




class Car():
    """
    Car class
    Author : Park ByeongHyeon
    Date : 2020 - 10 - 31
    """
    #클래스 변수(모든 인스턴스가 공유 하고 있음)
    car_count = 0



    def __init__(self,company,details): #인스턴스 변수
        self._company=company
        #self.car_count=10  이게 찾아지면 이걸 출력하고 이게 없으면 클래스변수에있나? 하고 클래스변수를 찾아본다
        self._details=details
        Car.car_count+=1

    def __str__(self):
        return "str : {} - {}".format(self._company,self._details)

    def __repr__(self):
        return "repr : {} - {}".foormat(self._company,self._details)

    def __del__(self):
        print("__del__ 함수에 들어갔어용~")
        Car.car_count-=1


    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get("price")))


car1=Car("Ferarri",{"color":"White","horsepower":400,"price":8000})
car2=Car("Bmw",{"color":"Black","horsepower":270,"price":5000})
car3=Car("Audi",{"color":"Silver","horsepower":300,"price":6000})
#Id 확인
print(id(car1))
print(id(car2))
print(id(car3))
print()

print(car1._company == car2._company)   #False
print(car1 is car2) #False
print()
#dir & __dict__ 확인
print(dir(car1))
print(dir(car2))
print()
print()
#dic 형태로 key 와 value값을 볼 수 있음
print(car1.__dict__)
print(car2.__dict__)
print()
#Doctoring(2~6 번째줄 에 있는 글이 나옴) 이런걸 달아주는게 하나하나 모여서 실력이 됨
print(Car.__doc__)
print()
#실행
car1.detail_info()
car2.detail_info()
print()
#비교
print(car1.__class__,car2.__class__)
print(id(car1.__class__),id(car2.__class__))    #main calss 의 id값이기 떄문에 값이 같게 나온다
print()

#에러
car1.detail_info()
#Car.detail_info() 라고 하면 에러가 남
Car.detail_info(car1) #윗 윗 줄과 같은 뜻
print()

#공유 확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)    #클래스 변수가 포함되지 않고 출력이 됨.
print(dir(car1)) #클래스 변수가 포함되어 출력됨
print()
#접근
print(car1.car_count)
print(Car.car_count)    #클래스 이름으로 접근하는게 정석이긴함
print()
del car2
#삭제 확인
print(Car.car_count)
#print(car1.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색을 함
# 즉, 동일한 이름으로 변수생성가능(인스턴스 검색후 -> 상위(클래스 변수, 부모 클래스 변수))
