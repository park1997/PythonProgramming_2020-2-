f=open('scores.txt','r').readlines()
result=[f[i].split() for i in range(len(f))]
for i in range(len(f)):
    score=float(result[i][2])*(0.2)+float(result[i][3])*(0.35)+float(result[i][4])*(0.45)
    grade=""
    if score>=85 and score<=100:
        grade="A"
    elif score<=84 and score>=75:
        grade="B"
    elif score<=74 and score>=50:
        grade="C"
    elif score<50:
        grade="D"
    print("Student ID\t: {}".format(result[i][0]))
    print("Student name\t: {}".format(result[i][1]))
    print("Total score\t: {}".format(score))
    print("Grade letter\t: {}".format(score))
    print("-"*30)
