def scalar_vector_product(scalar_v,vector_list):
    return [scalar_v*i for i in vector_list]
scalar_v=5
vector_list=[1,3,5,7,11,13]
print(scalar_vector_product(scalar_v,vector_list))
