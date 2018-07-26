from tkinter import *

window = Tk()

def kg_to_units():
    # print(e1_value.get())
    #miles = float(e1_value.get()) / 1.6
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

b1=Button(window, text="Convert", command=kg_to_units)
#both pack and grid work for button display
#b1.pack()
b1.grid(row=0, column=2)

e1_value=StringVar()
#entry means text box for user entry
# e1=Entry(window)
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

#add text widget 1
#t1=Text(window)
t1=Text(window, height=1,width=20)
t1.grid(row=1, column=0)

#add text widget 2
#t1=Text(window)
t2=Text(window, height=1,width=20)
t2.grid(row=1, column=1)

#add text widget 3
#t1=Text(window)
t3=Text(window, height=1,width=20)
t3.grid(row=1, column=2)


#this should always be at the end of 
window.mainloop()
