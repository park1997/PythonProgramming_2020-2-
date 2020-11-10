#3개 이상의 행렬의 곱이 가능한지 채점의 수월함을 위해 주석처리 해놓았습니다.
from functools import reduce
def matrix_mul(*z):
    return print(reduce(lambda x,y : [[sum(a*b for a,b in zip(r,c)) for c in zip(*y)]for r in x], z))
matrix_x=[[1,2,3],[4,5,6]]
matrix_y=[[1,2],[3,4],[5,6]]
#matrix_z=[[2,0],[0,2]]
#matrix_a=[[-1,0],[0,-1]]
#matrix_b=[[0,0],[0,0]]
matrix_mul(matrix_x,matrix_y)
#matrix_mul(matrix_x,matrix_y,matrix_z,matrix_a,matrix_b)
