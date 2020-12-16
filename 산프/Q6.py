# -*- coding: utf-8 -*-
"""
Student ID : 2017112502 (Young Woong Park)
"""

from tkinter import *
myGui = Tk()
myGui.geometry('450x200')
myGui.title('Q6 Program')

def convert_vowels():
    a = input_word_val.get()
    a=a.replace("a","!").replace("e","@").replace("i","#").replace("o","$").replace("u","%")
    print(a)
    return a

l1 = Label(myGui, text = "input your string/words: ")
l1.pack()

input_word_val = StringVar()
input_word = Entry(myGui, textvariable = input_word_val)
input_word.pack()

btn_convert = Button(myGui, text = "Convert the vowels", command = convert_vowels)
btn_convert.pack()

l2 = Label(myGui, text = "Result: ")
l2.pack()

output_word_val = StringVar()
output_word = Entry(myGui, textvariable = output_word_val)
output_word.pack()




myGui.mainloop()
