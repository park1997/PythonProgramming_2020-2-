col,row=map(int,input().split())
matrix=[]
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j]==".":
            cnt=0
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    if a<0 or b<0 or a>=row or b>=col:
                        continue
                    elif matrix[a][b]=="*":
                        cnt+=1
            matrix[i][j]=cnt
for i in matrix:
    for j in i:
        print(j,end="")
    print()
