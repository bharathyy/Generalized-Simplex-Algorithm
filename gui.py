import tkinter as tk
from tkinter import *
import gs

def str_to_int(x):
    for i in range(0,3):
        x[i] = int(x[i])
    return x

def solutionWindow():
    global e_z
    global e_1,e_2,e_3,e_b
    c = e_z.get()
    c = c.split()
    a1 = e_1.get()
    a1 = a1.split()
    a2 = e_2.get()
    a2 = a2.split()
    a3 = e_3.get()
    a3 = a3.split()
    b = e_b.get()
    b = b.split()
    c = str_to_int(c)
    a1 = str_to_int(a1)
    a2 = str_to_int(a2)
    a3 = str_to_int(a3)
    A = [a1,a2,a3]
    b = str_to_int(b)
    print(c,A,b)
    window.destroy()
    sol = gs.solution_(c,A,b)
    window2 = tk.Tk()
    window2.title("Generalized Simplex Method")
    label  =tk.Label(window2,text="GENERALIZED SIMPLEX METHOD ",font=("Helvetica",22),bg='#fbdcfe').pack(pady=20)
    label_sol = tk.Label(window2,text=sol,font=("Helvetica",18),bg='#fbdcfe').pack(pady=20)
    window2['bg']='#fbdcfe'
    window2.geometry("600x600")
    window2.mainloop()

window = tk.Tk()

e_z = StringVar()
e_1 = StringVar()
e_2 = StringVar()
e_3 = StringVar()
e_b = StringVar()

window.title("Generalized Simplex Method")
label  =tk.Label(window,text="GENERALIZED SIMPLEX METHOD ",font=("Helvetica",22),bg='#fbdcfe').pack(pady=20)

label_z = tk.Label(window,text="Enter Z Equation",font=("Helvetica",11),bg='#fbdcfe').place(x=100,y=100)
entry_z = tk.Entry(window,width=28,textvariable=e_z).place(x=300,y=100)

label_1 = tk.Label(window,text="Enter 1st Equation",font=("Helvetica",11),bg='#fbdcfe').place(x=100,y=150)
entry_1 = tk.Entry(window,width=28,textvariable=e_1).place(x=300,y=150)

label_2 = tk.Label(window,text="Enter 2nd Equation",font=("Helvetica",11),bg='#fbdcfe').place(x=100,y=200)
entry_2 = tk.Entry(window,width=28,textvariable=e_2).place(x=300,y=200)

label_3 = tk.Label(window,text="Enter 3rd Equation",font=("Helvetica",11),bg='#fbdcfe').place(x=100,y=250)
entry_3 = tk.Entry(window,width=28,textvariable=e_3).place(x=300,y=250)

label_b = tk.Label(window,text="Enter RHS of Equations",font=("Helvetica",11),bg='#fbdcfe').place(x=100,y=300)
entry_b = tk.Entry(window,width=28,textvariable=e_b).place(x=300,y=300)

bt = tk.Button(window,text="Find Solution",width=15,height=2,command=solutionWindow).place(x=250,y=450)

c = [0,0,-2]
A = [[1,-2,2], [-1, 1, 1], [2, -1, 4]]
b = [-8, 4, 10]

window['bg'] = '#fbdcfe'
window.geometry("600x600")
window.mainloop()


