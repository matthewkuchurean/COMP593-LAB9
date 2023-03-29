from tkinter import * 
from tkinter import ttk 

#Create a window 
root = Tk() 
root.title("Pokemon Information")

frm_top = ttk.Frame(root) 
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.Frame(root)
frm_btm_left.grid(row=1, column=0) 

frm_btm_right = ttk.Frame(root)
frm_btm_right.grid(row=1, column=1) 