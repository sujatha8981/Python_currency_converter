
import tkinter as tk
from tkinter import *

OptionList1 = [
"USA Dallas",
"Indian rupee",
"Nigeria naira",
"Canadian dollar",
"Brazillian real",
"Kenya kenyan shilling",
"Euro",

]
 
def Ok():
 
    to = variable1.get()
 
    amount = float(e1.get())
 
    if ( to == "USA Dallas"):
 
        tot = amount * 1.34
 
    elif (to == "Indian rupee"):

        tot = amount * 89.03

    
    elif (to == "Canadian dollar"):

        tot = amount * 1.72

    
    elif (to == "Brazillian real"):

        tot = amount * 4.31

    
    elif (to == "Kenya kenyan shilling"):

        tot = amount * 135.89

    else:

        tot = amount * 1.19
 
    nsalText.set(tot)
 
root = tk.Tk()
root.geometry('800x500')
root.title("Currency Converter")
root.configure(bg='gray81')
root.config(highlightcolor='white')


canvas_width = 600
canvas_height =500
python_green = "#476042"

w = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='lightpink',width=3)



variable1 = tk.StringVar(root)
variable1.set(OptionList1[0])
 
opt = tk.OptionMenu(root,variable1, *OptionList1).place(x=710,y=250)


 
global e1
global nsalText
nsalText = tk.StringVar()

 


tk.Label(root, text="Currency Converter",font=('Times new roman', 30,'bold','underline'), fg='whitesmoke',bg='black',bd=2,width=25).place(x=380, y=3)

tk.Label(root, text="British pound equals",font=('Times new roman', 14,'bold'), fg='red',relief=RAISED,bd=2,width=18).place(x=400, y=200)
 
tk.Label(root, text="Choose Country",font=('Times new roman', 14,'bold'), fg='red',relief=RAISED,bd=2,width=18).place(x=400, y=250)
tk.Label(root, text="", font=('Times new roman', 20,'bold'), fg='red' ,height=3,width=20,bd=5,bg='whitesmoke', textvariable=nsalText).place(x=650, y=400)
tk.Button(root, text="Convert",font=('Times new roman', 14,'bold'), command=Ok ,height = 2, width = 8).place(x=420, y=380)
 
e1 = tk.Entry(root,relief=RAISED,bd=2,width=20)
e1.place(x=700, y=200)
 

root.mainloop()
