import pandas as pd
class Student:
    def __init__(self,informa):
        self.name, self.number, self.department, self.math, self.english, self.korean=informa
    def info(self):
        name=self.name
s1=Student([1,2,3,4,5,6])
print(s1.name)
