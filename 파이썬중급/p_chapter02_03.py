class Car():
    """
    Car Class
    Author : Park
    Date : 2021.02.15
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든인스턴스가 공유함)
    car_count = 0 

    def __init__(self,company,details):
        self._company = company
        self._details = details
        # self.car_count =10


    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return "str : {} - {}".format(self._company,self._details)

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get("price")))


# self 의미
car1 = Car('Ferrari',{'color':'White',"horsepower":400,"price":8000})
car2 = Car('Bmw',{'color':'Black',"horsepower":270,"price":5000})
car3 = Car('Audi',{'color':'Silver',"horsepower":300,"price":6000})
