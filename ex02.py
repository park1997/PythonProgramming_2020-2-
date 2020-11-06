print("Welcome to the Course Manager v1.0")
result=[]
while 1:
    print()
    print("Please input the # of the course : ",end="")
    a=int(input())
    if a>5:
        print("Sorry, you have to input the # od courses, maximum is 5 only! ")
    else:
        while len(result)!=a :
            print()
            print("Please type the course name :",end="")
            result.append(input())
    if len(result)==a:
        break
if a<=5:
    print("Course list : {}".format(result))
    fname = open("course_list.txt", mode = "w")
    for i in result:
        fname.write(i)
        fname.write("\n")
    print("The course list is saved in course_list.txt")
fname.close()
