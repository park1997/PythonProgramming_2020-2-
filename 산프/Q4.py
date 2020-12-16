#2017112513 이지섭
from tkinter import*
import tkinter.messagebox
root = Tk()
root.geometry("700x100")
root.title("Q4 Program")

num = Label(root, text = "Input Numbers: ")
num.grid(row=0, column=0)
input_num = Entry(root)
input_num.grid(row=0, column=1)


def sum():
    try:
        total = 0
        numbers = map(int,input_num.get().split(','))
        list_number = list(numbers)
        for x in list_number:
            total = total + x
        result.set(int(total))
    except:
        if input_num.get() == '':
            tkinter.messagebox.showerror(title = "Input empty", message = "Input should not be empty!")
        else:
            tkinter.messagebox.showerror(title = "Please input number only!", message = "Please input number only!")
def average():
    try:
        total = 0
        numbers = map(int,input_num.get().split(','))
        list_number = list(numbers)
        for x in list_number:
            total = total+x
        average = total/len(list_number)
        result.set(average)
    except:
        if input_num.get() == '':
            tkinter.messagebox.showerror(title = "Input empty", message = "Input should not be empty!")
        else:
            tkinter.messagebox.showerror(title = "Please input number only!", message = "Please input number only!")

def variance():
    try:
        different_sum = 0
        total = 0
        numbers = map(int,input_num.get().split(','))
        list_number = list(numbers)
        for x in list_number:
            total = total+x
        average = total/len(list_number)
        for i in list_number:
            different = (i-average)**2
            different_sum = different_sum + different
        variance = different_sum / len(list_number)
        result.set(variance)
    except:
        if input_num.get() == '':
            tkinter.messagebox.showerror(title = "Input empty", message = "Input should not be empty!")
        else:
            tkinter.messagebox.showerror(title = "Please input number only!", message = "Please input number only!")
def standard():
    try:
        different_sum = 0
        total = 0
        numbers = map(int,input_num.get().split(','))
        list_number = list(numbers)
        for x in list_number:
            total = total+x
        average = total/len(list_number)
        for i in list_number:
            different = (i-average)**2
            different_sum = different_sum + different
        variance = different_sum / len(list_number)
        standard = variance**(1/2)
        result.set(standard)
    except:
        if input_num.get() == '':
            tkinter.messagebox.showerror(title = "Input empty", message = "Input should not be empty!")
        else:
            tkinter.messagebox.showerror(title = "Please input number only!", message = "Please input number only!")

B1 = Button(root,width=7,height=1, text = "Total", command = sum)
B1.grid(row=1,column=0)
B2 = Button(root,width=7,height=1, text = "Avg", command = average)
B2.grid(row=1,column=1)
B3 = Button(root,width=7,height=1, text = "variance", command = variance)
B3.grid(row=1,column=3)
B4 = Button(root,width=7,height=1, text = "Standard Deviation", command = standard)
B4.grid(row=1, column=2)
L1 = Label(root, text = "Result : ")
L1.grid(row=2,column=0)
result = StringVar()
ans = Entry(root, textvariable = result)
ans.grid(row=2, column=1)

root.mainloop()
