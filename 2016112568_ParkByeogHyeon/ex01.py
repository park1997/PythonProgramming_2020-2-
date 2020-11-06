def matrix_mul(x,y,*z):
    num=len(z)
    if len(z)==0:
        result=[[sum(a*b for a,b in zip(r,c)) for c in zip(*y)] for r in x]
        return print(result)
    elif num!=0:
        matrix_mul(result,z[0])
        num-=1
matrix_x=[[1,2,3],[4,5,6]]
matrix_y=[[1,2],[3,4],[5,6]]
matrix_mul(matrix_x,matrix_y)
