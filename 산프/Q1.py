from tkinter import *

Q5=Tk()
Q5.geometry("270x150")
Q5.title("Q5 Program")

label1=Label(Q5, text="input your score:")
label1.grid(row=0, column=0)

your_score=Entry(Q5)
your_score.grid(row=0, column=1)

def Q5_func():
    score=your_score.get()
    try:
        score=int(score)
        if 85<=score<=100:
            score="A"
        elif 75<=score<=84:
            score="B"
        elif 50<=score<=74:
            score="C"
        else:
            score="D"
    except:
        if len(score)==0:
            messagebox.showwarning(title="Input empty", message="Input should not be empty!")
        else:
            messagebox.showwarning(title="Input empty", message="Please input number only!")




    result_val.set(str(score))

btn_Q5=Button(Q5, text="Convert to letter", command=Q5_func)
btn_Q5.grid(row=2, column=1)

label3=Label(Q5, text="Result:")
label3.grid(row=3, column=0)

result_val=StringVar()
result=Entry(Q5, textvariable=result_val)
result.grid(row=3, column=1)


Q5.mainloop()
