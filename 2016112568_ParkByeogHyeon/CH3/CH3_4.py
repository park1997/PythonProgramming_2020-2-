# 01
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])

#02
a = [0, 1, 2, 3, 4]
print(a[::-1])

#03
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)

#04
list_a = [3, 2, 1, 4]
list_b = list_a.sort()
print(list_a, list_b)

#05
a = [5, 7, 3]
b = [3, 9, 1]
c = a + b
c = c.sort()
print(c)

#07
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])

#08
num = [1, 2, 3, 4]
print(num * 2)

#09
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']

a.append('g')
b.append(6)
print('g' in b, len(b))

#12
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)

#15
a = [5,4,3,2,1]
b = a
c = [5,4,3,2,1]
print(a is b)
print(a is c)
