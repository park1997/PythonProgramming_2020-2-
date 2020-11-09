def scalar_vector_product(scalar_v,vector_list):
    return [scalar_v*i for i in vector_list]



scalar_v=int(input())
vector_list=list(map(int,input().split()))


print(scalar_vector_product(scalar_v,vector_list))
