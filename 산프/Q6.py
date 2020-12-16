# -*- coding: utf-8 -*-
"""
Student ID : 2017112502 (Young Woong Park)
"""

from tkinter import *
myGui = Tk()
myGui.geometry('450x200')
myGui.title('Q6 Program')

l1 = Label(myGui, text = "input your string/words: ")
l1.pack()

input_word_val = StringVar()
input_word = Entry(myGui, textvariable = input_word_val)
input_word.pack()

def convert_vowels():
    string_word = input_word_val.get()
    if string_word == "":
        messagebox.showerror(title = "Input empty", message = "Input should not be empty!")
    else:
        st = string_word.replace("a","!").replace("e","@").replace("i","#").replace("o","$").replace("u","%")
        output_word_val.set(st)


btn_convert = Button(myGui, text = "Convert the vowels", command = convert_vowels)
btn_convert.pack()

l2 = Label(myGui, text = "Result: ")
l2.pack()

output_word_val = StringVar()
output_word = Entry(myGui, textvariable = output_word_val)
output_word.pack()






myGui.mainloop()
