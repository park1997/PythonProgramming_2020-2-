def matrix_add(*x):
    return print([[sum(j) for j in zip(*i)] for i in zip(*x)])
matrix_x=[[2,5],[2,1],[3,5]]
matrix_y=[[3,4],[5,6],[7,8]]
matrix_add(matrix_x,matrix_y)
