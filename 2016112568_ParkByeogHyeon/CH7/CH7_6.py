from collections import Counter
f=open('대한민국헌법_1장.txt','r')
result=""
for i in f.readlines():
    result+=i
f.close()
result=result.replace("①"," ").replace("②"," ").replace("③"," ").replace("④"," ").replace("⑤"," ").replace("⑥"," ").replace("⑦"," ")
real_result=result.replace("["," ").replace("]"," ").replace("."," ").replace("ㆍ"," ").split()
print(Counter(real_result).most_common(10))
