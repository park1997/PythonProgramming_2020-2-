from functools import reduce
def matrix_mul(*args):
    result=reduce(lambda x,y : [[sum(a*b for a,b in zip(i,j))for j in zip(*y)]for i in x], args)
    return result

matrix_x=[[1,2,3],[4,5,6]]
matrix_y=[[1,2],[3,4],[5,6]]
matrix_z=[[-1,0],[0,-1]]
print(matrix_mul(matrix_x,matrix_y,matrix_z))
