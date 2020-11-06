def mul(*values):
    a=1
    for i in values:
        a*=i
    return a
print(mul(5,7,9,10))
