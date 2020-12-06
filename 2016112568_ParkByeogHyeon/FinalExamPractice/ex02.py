def add_mul(s,A,B,C):
    result=[[s*j for j in i] for i in A]
    result=[[sum(j) for j in zip(*i)] for i in zip(result,B)]
    result= [[sum(i*j for i, j in zip(r_r,C_c)) for C_c in zip(*C)] for r_r in result]
    return result


s_sclar =5
matrix_a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix_b=[[11,12,13,14],[15,16,17,18],[19,20,21,22]]
matrix_c=[[1,0,1,0],[0,2,0,2],[3,0,3,0],[0,4,0,4]]

matrix_res = add_mul(s_sclar,matrix_a,matrix_b,matrix_c)
print(matrix_res)
