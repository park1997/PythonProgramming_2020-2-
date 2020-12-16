# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:51:55 2020

@author: 이찬규(2017112559)
"""

from calculate import Calculation

def main():

    start = int(input("please input number 1  :"))
    end = int(input("please input number 2  :"))

    number = Calculation(start,end)

    print("Number 1 is " , number.start)
    print("Number 2 is " , number.end)
    print("{} x {} is {}".format(number.start,number.end,number.get_multiplecation()))
    print("{} + {} is {}".format(number.start,number.end,number.get_addition()))
    print("{} - {} is {}".format(number.start,number.end,number.get_subtraction()))
    print("{} / {} is {}".format(number.start,number.end,number.get_division()))

main()
