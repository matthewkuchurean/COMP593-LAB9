from tkinter import * 
from tkinter import ttk 
#from 
#Create a window 
# Create the window


def handle_getinfo():
    poke_name =ent_name.get()
    poke =ent_name.get().strip()
    if len(poke_name) == 0:
        return 
    
    #poke information from pokemon API 
    poke_info = get_pokemon(poke_name)
    if poke_info is None:
            



    #bar_hp['value'] = poke_info ['stats'][0]['base_stats']
    #bar_attack['value'] = poke_info ['stats'][1]['base_stats']
    #bar_defence['value'] = poke_info ['stats'][2]['base_stats']
    #bar_sA['value'] = poke_info ['stats'][3]['base_stats']
    #bar_sD['value'] = poke_info ['stats'][4]['base_stats']
    #bar_speed['value'] = poke_info ['stats'][5]['base_stats']



    return



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

# Populate the info
lbl_height_value['text] = f"{'poke_info['height]}dm"
                                  


#Title Frame 
# Add Widgets to frames 
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0 , padx= (30) ,pady= (30))

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(10,20), pady=(10,20))

btn_hello = ttk.Button(frm_top, text='Get Info', command=handle_getinfo)
btn_hello.grid(row=0, column= 2, padx=15, pady=20)

#Info of Pokemon Frame 
# Info frame in the populate widget 
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx= 10 , pady= 20)

lbl_hp= ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx= 5 , pady= 5) 

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx= 10 , pady= 20)

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx= 10 , pady= 20)

#Stats Frame labels and Bars 
#Stats of Pokemon 

lbl_hp= ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx= 5 , pady= 5) 
lbl_hp= ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx= 5 , pady= 5) 
lbl_hp= ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx= 5 , pady= 5) 
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
bar_hp.grid (row=0, column=1)
bar_hp['value'] = 123

# ATTACK LABELS AND BARS 
lbl_attack= ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, padx= 5 , pady= 5)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
bar_attack.grid (row=1, column=1)
bar_attack['value'] = 255

#DEFENCE LABELS AND ROWS 
lbl_defence= ttk.Label(frm_btm_right, text='Defence:')
lbl_defence.grid(row=2, column=0, padx= 10 , pady= 5)
bar_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
bar_defence.grid (row=2, column=1)
bar_hp['value'] = 255

#SPECIAL ATTACK LABELS AND ROWS 
lbl_sA= ttk.Label(frm_btm_right, text='Special Attack:')
lbl_sA.grid(row=3, column=0, padx= (10,20) , pady= (10,20))
bar_sA = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
bar_sA.grid (row=3, column=1)
bar_hp['value'] = 244


#SPECIAL DEFENCE LABELS AND ROWS 
lbl_sD= ttk.Label(frm_btm_right, text='Special Defence:')
lbl_sD.grid(row=4, column=0, padx= 10 , pady= 5)
bar_sD = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
bar_sD.grid (row=4, column=1)
bar_hp['value'] = 222


# SPECIAL SPEED LABELS AND ROWS 
lbl_speed= ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, padx= 10 , pady= 5)
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum =255)
bar_speed.grid (row=5, column=1)
bar_hp['value'] = 111


# TODO: Add weight and height 
root.mainloop()

