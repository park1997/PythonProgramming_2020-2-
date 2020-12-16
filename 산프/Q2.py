class Student:
    def __init__(self,num,name,status):
        self.num=num
        self.name=name
        self.status=status

    def showResponsibility(self):
        print("{}".format("-"*30))
        print("{}\t\t: {}".format("Student ID",self.num))
        print("{}\t\t\t: {}".format("Name",self.name))
        print("{}\t\t\t: {}".format("Status",self.status))
        print("{}\t\t: {}".format("Responsibility","Study, take the exams"))
        print("{}".format("-"*30))
        print()


class GradStudent(Student):
    def __init__(self,num,name,status):
        self.num=num
        self.name=name
        self.status=status

    def showResponsibility(self):
        print("{}".format("-"*30))
        print("{}\t\t: {}".format("Student ID",self.num))
        print("{}\t\t\t: {}".format("Name",self.name))
        print("{}\t\t\t: {}".format("Status",self.status))
        print("{}\t\t: {}".format("Responsibility","Study, take the exams, and writind thesis"))
        print("{}".format("-"*30))
        print()

def main():
    std1=Student(202011,"michael","undergraduate")
    std2=GradStudent(202012,"jack","doctoral")

    std1.showResponsibility()
    std2.showResponsibility()


main()
