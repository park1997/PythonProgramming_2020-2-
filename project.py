import numpy as np
import time
arr = np.array(range(100)).reshape((20,-1))
num = 0
def fucking_cycle(arr_df,input_arr,cycle=20):
    global num
    if len(arr_df)<20:
        return
    else:
        arr_df[num%cycle] = input_arr
        return arr_df
while 1:
    # while 1 싸이클당 5개의 인풋이들어옴
    input = np.array([num]*5) # 5개의 가상의 인풋값
    arr = fucking_cycle(arr,input)
    num+=1  
    print(arr)
    time.sleep(1)
    # if num >40:
    #     break
