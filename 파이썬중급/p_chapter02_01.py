# Chapter02-01
# 객체지향 프로그래밍(oop) 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 
# 규모가 큰 프로젝트(프로그램) -> 함수 중심
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

car_company_1 = "Ferarri"
car_datail_1=[{"color":"White"},{"horsepower":400},{"price":8000}]

car_company_2 = "Bmw"
car_datail_2=[{"color":"Black"},{"horsepower":270},{"price":5000}]

car_company_3 = "Audi"
car_datail_3=[{"color":"Silver"},{"horsepower":300},{"price":6000}]


# list Struc
# 관리하기가 불편
# 인덱스로 접근해야함(실수 유발), 삭제가 불편함
car_company_list = ["Ferarri","Bmw","Audi"]
car_detail_list = [{"color":"White","horsepower":400,"price":8000},{"color":"Black","horsepower":270,"price":5000},{"color":"Silver","horsepower":300,"price":6000}]

del car_company_list[car_company_list.index("Ferarri")]  
print(car_company_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩문제(키는 중첩 될 수 없음)

car_dicts=[{"car_company": "Ferarri","car_datail":{"color":"White","horsepower":400,"price":8000},"car_company": "Bmw","car_datail":{"color":"White","horsepower":270,"price":5000},"car_company": "Audi","car_datail":{"color":"Silver","horsepower":300,"price":6000}}]


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화
# 메소드 활용

class Car():
    def __init__(self,company,details):
        self._company = company
        self._details = details

    # 내 코딩이 잘 되고있는 건가 문자열을 출력해줌
    # def __str__(self):
    #     return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        # __str__ 이 없으면 __repr__ 을 출력함
        return 'str : {} - {}'.format(self._company,self._details)

    def __reduce__(self):
        pass


car1 = Car('Ferrari',{'color':'White',"horsepower":400,"price":8000})
car2 = Car('Bmw',{'color':'Black',"horsepower":270,"price":5000})
car3 = Car('Audi',{'color':'Silver',"horsepower":300,"price":6000})
print("1. ")
# def __repr__ 로 인식되어 나옴
# repr => representation
print(car1)
print(car2)
print(car3)

print()
print("2.")
# 객체 안에 뭐가 들었지? 중간중간에 확인 가능 !!
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print("3.")
print(dir(car1))

print()
print("4.")

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print("5.")

for i in car_list:
    # print(repr(i)) # 이렇게 repr를 사용하려 호출도 가능
    print(i)
