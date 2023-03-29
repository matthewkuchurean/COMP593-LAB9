from tkinter import * 
from tkinter import ttk 

#Create a window 
# Create the window
root = Tk()
root.title("Pokemon Information Viewer ")
# TODO: Additional window configuration

# TODO: Add Frames to window

frm_top = ttk.Frame(root) 
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.LabelFrame(root, text = 'Info of Pokémon')
frm_btm_left.grid(row=1, column=0) 

frm_btm_right = ttk.LabelFrame(root, text = 'Stats of the Pokémon')
frm_btm_right.grid(row=1, column=1) 

# Add Widgets to frames 
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0 , padx= (10,20) ,pady= (10,20))

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(10,20), pady=(10,20))

def handle_getinfo():
    return

btn_hello = ttk.Button(frm_top, text='Get Info', command=handle_getinfo)
btn_hello.grid(row=0, column= 2, padx=15, pady=20)


root.mainloop()

