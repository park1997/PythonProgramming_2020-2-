def f(x):
    result=[]   #재귀호출될때마다 result 빈list로 초기화
    for i in x:
        if type(i) is list:
            result+=f(i)    #뽑은게 리스트면 벗기기위해 재귀호출
        else:
            result.append(i)
    return result
example =[[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:",example)
print("변환:",f(example))
