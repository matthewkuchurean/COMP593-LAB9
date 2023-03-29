from tkinter import * 
from tkinter import ttk 
#from 
#Create a window 
# Create the window


def handle_getinfo():
    #poke_name =ent_name.get()
    #poke information from pokemon API 
    #poke_info = get_pokemon_info()
    return

# lbl_height_value ['text] = f"{'poke_info['height]}dm"
#bar_hp['value']
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


btn_hello = ttk.Button(frm_top, text='Get Info', command=handle_getinfo)
btn_hello.grid(row=0, column= 2, padx=15, pady=20)

# Info frame in the populate widget 
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx= 10 , pady= 20)

lbl_hp= ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx= 10 , pady= 20) 

#Widget for stats frame 
#bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
#bar_hp.grid (row=1, column=1)
#bar_hp['value'] = 123

#lbl_attack= ttk.Label(frm_btm_right, text='Attack:')
#lbl_attack.grid(row=1, column=1, padx= (10,20) , pady= (10,20))
#bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
#bar_attack.grid (row=1, column=0)

#lbl_defence= ttk.Label(frm_btm_right, text='Defence:')
#lbl_defence.grid(row=0, column=1, padx= (10,20) , pady= (10,20))
#bar_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
#bar_defence.grid (row=1, column=0)



# TODO: Add weight and height 
#root.mainloop()

