class person:
    count=0
    def __init__(self):
        person.count+=1 #인스턴스가 만들어질떄 클래스 속성 count 에 1을 더함
    @classmethod
    def print_count(cls):
        print("{}명 생성되었습니다".format(cls.count))
    @classmethod
    def create(cls):
        p=cls()
        return p

james=person()
maria=person()

person.print_count()
