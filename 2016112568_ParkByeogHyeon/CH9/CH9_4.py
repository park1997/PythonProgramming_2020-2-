from functools import reduce
def vector_sub(*v):
    return print([reduce(lambda x,y:x-y,i) for i in zip(*v)])
vector_sub([1,3],[2,4])
vector_sub([1,5],[10,4],[4,7])
vector_sub([10,9,8],[1,2,3],[3,4,5],[1,1,1])
