from tkinter import*

def area_triangle():
        a=float(ent1.get())
        b=float(ent2.get())
        c=float(ent3.get())
        p=(a+b+c)/2
        s=(p*(p-a)*(p-b)*(p-c))**0.5
        lab_result["text"]=str(s)+" m2"

root=Tk()
root.geometry("250x220")

ent1=Entry(root, width=10)
ent2=Entry(root, width=10)
ent3=Entry(root, width=10)
ent1.grid(row=0, column=1, padx=6, pady=16)
ent2.grid(row=1, column=1, padx=6, pady=16)
ent3.grid(row=2, column=1, padx=6, pady=16)

lab1=Label(root, text="Insert side A")
lab2=Label(root, text="Insert side B")
lab3=Label(root, text="Insert side C")
lab1.grid(row=0, column=0, padx=6, pady=16)
lab2.grid(row=1, column=0, padx=6, pady=16)
lab3.grid(row=2, column=0, padx=6, pady=16)

btn=Button(root, text="Count", width=10, bg="pink", command=area_triangle)
btn.grid(row=5, column=1, padx=6, pady=6)

lab_result=Label(root, text="")
lab_result.grid(row=8, column=1)

root.mainloop()
