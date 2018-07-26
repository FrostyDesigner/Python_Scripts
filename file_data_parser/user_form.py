#tkinter is the gui library
from tkinter import *

#try to import another python script
import file_data_parser as fdp

#method to call other script
def call_the_parser():
    src_file = tb_src_value.get()
    dest_file = tb_dest_value.get()
    if src_file == "" or dest_file == "":
        print("Application needs a source file and a destination file location.")
        return
    fdp.parse_data(src_file, dest_file)


window = Tk()
window.minsize(300,80)
window.maxsize(400,80)
window.geometry("300x80")

#create a label and put it in the first row and first column
lbl_src=Label(window,text="Source File")
lbl_src.grid(row=0,column=0)

#create a label and put it in the second row and first column
lbl_dest=Label(window,text="Destination File")
lbl_dest.grid(row=1,column=0)

#create variable to hold user entry
tb_src_value=StringVar()
#entry means text box for user entry
# tb_src=Entry(window)
tb_src=Entry(window, textvariable=tb_src_value)
tb_src.grid(row=0,column=1)
tb_src.focus_set()

#create variable to hold user entry
tb_dest_value=StringVar()
tb_dest=Entry(window, textvariable=tb_dest_value)
tb_dest.grid(row=1,column=1)

#create a button and put it in the third row and second column
b1=Button(window, text="Parse", command=call_the_parser)
#both pack and grid work for button display
#b1.pack()
b1.grid(row=2, column=1)

#use these to test entries
#tb_src.insert(0, r"C:\GitHub\Python_Scripts\data_file_parser\directory_scan.txt")
#tb_dest.insert(0, r"C:\GitHub\Python_Scripts\data_file_parser\files.csv")

#this should always be at the end of 
window.mainloop()
