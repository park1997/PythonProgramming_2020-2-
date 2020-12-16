def employee_input():
    while 1:
        a=int(input("Please input the # of employee: "))
        if a>3:
            print("Sorry, you have to input the # of employee, maximum is 3 only!")
            print()
        else:
            break
    emp_list=[]
    for i in range(a):
        input_name=input("Name: ")
        print()
        input_position=input("Position: ")
        print()
        emp_list.append([input_name,input_position])
    return emp_list
def get_salary(position):
    salary=0
    if position=="manager":
        salary=3500
    elif position=="staff":
        salary=3000
    return salary


def main():
    print("Welcome to Employee Manager v1")
    print()
    employee_list = employee_input()

    filename = "employees.txt"
    cFile=open(filename,"w")

    for c in employee_list:
        name = "Name\t\t : "+str(c[0])
        pos = "Position\t: "+str(c[1])
        salary = "Salary\t\t: $"+str(get_salary(c[1]))
        line = "--"*15
        cFile.write(name+"\n")
        cFile.write(pos+"\n")
        cFile.write(salary+"\n")
        cFile.write(line+"\n")



    cFile.close()
    print("The emplyee list is saved in ",filename)

main()
