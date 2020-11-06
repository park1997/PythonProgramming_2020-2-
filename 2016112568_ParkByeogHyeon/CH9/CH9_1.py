from functools import reduce
while 1:
    a=int(input())
    if a>=10 and a<=50:
        print("{:,}".format(reduce(lambda x,y: x*y,range(1,a+1))))
        break
    else:
        print("10 이상 50 이하의 수로 재 입력 하세요. : ", end="")
