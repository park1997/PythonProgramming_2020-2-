# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:19:03 2020

@author: 이찬규(2017112559)
"""

class Calculation:

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def get_multiplecation(self):
        return self.start * self.end

    def get_addition(self):
        return self.start + self.end

    def get_subtraction(self):
        return self.start - self.end

    def get_division(self):
        return self.start / self.end

        
