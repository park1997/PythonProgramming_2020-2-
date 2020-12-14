a=(1,2,5,4,3,2,9,4,7,8,9,9,3,7,3)
result={}
for i in a:
    if i not in result:
        result[i]=1
    else:
        result[i]+=1
result=sorted(result.items(), key=lambda x:x[1], reverse=True)
max_num=result[0][1]
real=[i[0] for i in result if i[1]==max_num]
print("입력 : 주어진 튜플 : ",a)
print("출력 : 중복 제거 튜플 : ",tuple(set(a)))
print("       가장 많은 중복 요소 : ",max(real))
