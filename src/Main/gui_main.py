import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
#import prep_menu
from prep_menu import data_update_prep_stock
#import file_clean
from file_clean import export_data

from prep_menu import prep_menu_items, MenuItem, add_quantity, get_quantity, set_quantity, get_name, get_path

"""
dictionary linking menu objects to a row in GUI
    {menuitem:menu_item_frame}
"""
menu_gui_dict = {}

"""
dictionary of photoimage items used by menu items
    {menuitem:image}
"""
menu_images = {}

class MenuItemFrame():
    """
    Frames representing each item on the prep menu.
    Frames are linked to their item at init. 
        However, a dictionary is used to link items back to their frames.
    """
    def __init__(self,item:MenuItem):
        self.menu_item = item
        self.the_frame = tk.Frame(main_frame, bg="#CCE5FF", bd=2, width=780, height=120)
        #row's image: resize to 100*100
        temp_img = Image.open(get_path(item))
        resize = temp_img.resize((100, 100))
        tk_img = ImageTk.PhotoImage(resize)   
        menu_images.update({item:tk_img})
        self.img_label = tk.Label(self.the_frame, image=menu_images.get(item))
        self.img_label.pack(side=LEFT, padx=4)

        #row's name label
        self.name_label = tk.Label(self.the_frame, text=get_name(item), fg='#007FFF')
        self.name_label.pack(side=LEFT, padx=10)
        #row's quantity label
        self.quan_label = tk.Label(self.the_frame, text=str(get_quantity(item)), fg='#007FFF')
        self.quan_label.pack(side=LEFT, padx=12)
        #row's add button
        self.add_bttn = tk.Button(self.the_frame,text='+', bg='green', fg='white', command=lambda: crement_button_click(self.menu_item,FALSE))
        self.add_bttn.pack(side=LEFT, padx=5)
        #row's subtract button
        self.minus_bttn = tk.Button(self.the_frame,text='-', bg='red', fg='white', command=lambda: crement_button_click(self.menu_item,TRUE))
        self.minus_bttn.pack(side=LEFT, padx=5)

        menu_gui_dict.update({item:self})
    
def crement_button_click(item:MenuItem,flag:bool):
    add_quantity(item,1,flag)
    update_single_stock(item)

#display mass stock updates from file data
def update_stock_labels():
    data_update_prep_stock(export_data())
    for item in menu_gui_dict:
        update_single_stock(item)
    root.after(10000, update_stock_labels) # run itself again after 10 sec

#display individual stock updates
def update_single_stock(item:MenuItem):
#    print("button clicked!")
    new_quan = get_quantity(item)
    print(type(item),": ",str(new_quan))
    menu_gui_dict.get(item).quan_label.configure(text=str(new_quan))

#root user interface script
root = tk.Tk()
root.title("Prep Food Counter")
root.geometry('800x600')
root.maxsize(800,600)

    #scrollable canvas
canvas = tk.Canvas(root, bg='gray')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

    #scrollbar
scroll_bar = tk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scroll_bar.set)

main_frame = tk.Frame(canvas, bg='black')
canvas.create_window((400,0), window=main_frame, anchor='n')

    #Scroll action
main_frame.bind("<Configure>",lambda e: canvas.config(scrollregion= canvas.bbox(ALL)))

    #Root window title label
title = tk.Label(main_frame, text='Prep Stock', fg='#007FFF')
title.pack()

    #Lastest update time label
latest_update = tk.Label(main_frame, text=datetime.now().strftime("%d-%m-%Y | %H:%M"), fg='#007FFF')
latest_update.pack()

    #Add each frame to the root window
for item in prep_menu_items:
    new_frame = MenuItemFrame(item)
#    print(type(item))
    new_frame.the_frame.pack(padx=20, pady=5)

#execute gui
update_stock_labels()
root.mainloop()
#print(menu_gui_dict)