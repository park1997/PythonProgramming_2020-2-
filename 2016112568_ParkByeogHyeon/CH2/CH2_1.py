a=777
b=777
print(a==b,a is b)
#result:True True
a=3.5
b=int(3.5)
print(a**((a//b)*2))
#result:12.25
print(((a-b)*a)//b)
#result:0.0
b=(((a-b)*a)%b)
print(b)
#result:1.75
print((a*4)%(b*4))
#result:0.0
