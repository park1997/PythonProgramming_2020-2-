class Employee:
    def __init__(self,name,department,position):
        self.name=name
        self.department=department
        self.position=position
        if self.position=="manager" and self.department=="accounting":
            self.salary=2500
        elif self.position=="staff" and self.department=="accounting":
            self.salary=2000
        elif self.position=="manager" and self.department=="rnd":
            self.salary=3500
        elif self.position=="staff" and self.department=="rnd":
            self.salary=3000
    def showEmployee(self):
        print("{}".format("-"*30))
        print("{}\t\t: {}".format("Name",self.name))
        print("{}\t: {}".format("Department",self.department))
        print("{}\t: {}".format("Position",self.position))
        print("{}\t\t: $ {}".format("Salary",self.salary))
        print("{}".format("-"*30))
        print()

def main():
    emp1=Employee("John","accounting","manager")
    emp2=Employee("James","accounting","staff")
    emp3=Employee("Jackson","rnd","manager")
    emp4=Employee("Jane","rnd","staff")

    emp1.showEmployee()
    emp2.showEmployee()
    emp3.showEmployee()
    emp4.showEmployee()

main()
