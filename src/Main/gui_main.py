import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

from prep_menu import prep_menu_items, MenuItem, add_quantity, get_quantity, set_quantity, get_name, get_path

"""
dictionary linking menu objects to a row in GUI
    {menuitem:frame}
"""
menu_gui_dict = {}

"""
dictionary of photoimage items used by menu items
    {menuitem:image}
"""
menu_images = {}

#crement buttons functions: manual stock updates
def add_btn_click():
    print("+")
    add_quantity(item,1,FALSE)

def minus_btn_click():
    print("-")
    add_quantity(item,1,TRUE)

#display mass stock updates
def update_stock_labels(items:dict):
    for item in menu_gui_dict:
#        print("item's type is: " +str(type(item)))
        new_quan = get_quantity(item)
        menu_gui_dict.get(item).quan_label.configure(text=str(new_quan))
    root.update()
#    pass

#display individual stock updates
def update_single_stock(item:MenuItem):
    print("button clicked!")
    new_quan = get_quantity(item)
    menu_gui_dict.get(item).quan_label.configure(text=(str(new_quan)))

#user interface script
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

    #Create row-frames for each menu item
    #Give each frame the attributes of the components for later reference
for item in prep_menu_items:  
    new_frame = tk.Frame(main_frame, bg="#CCE5FF", bd=2, width=780, height=120)
    #row image: resize to 100*100
    temp_img = Image.open(get_path(item))
    resize = temp_img.resize((100, 100))
    tk_img = ImageTk.PhotoImage(resize)   
    menu_images.update({item:tk_img})
    new_frame.img_label = tk.Label(new_frame)

    #row name label
    new_frame.name_label = tk.Label(new_frame)
    #row quantity label
    new_frame.quan_label = tk.Label(new_frame)
    #row add button
    new_frame.add_bttn = tk.Button(new_frame)
    #row subtract button
    new_frame.minus_bttn = tk.Button(new_frame)

    menu_gui_dict.update({item:new_frame})

    #Fill the created frames with all thier components: pack frames horizontally
for menu_item in menu_gui_dict:
#    print("menu_item's type is: "+str(type(menu_item)))
    current_frame = menu_gui_dict.get(menu_item)
    #picture on the left
    current_frame.img_label.configure(image=menu_images.get(menu_item))
    current_frame.img_label.pack(side=LEFT, padx=4)

    #name of the food
    current_frame.name_label.configure(text=get_name(menu_item), fg='#007FFF')
    current_frame.name_label.pack(side=LEFT, padx=10)

    #number of food available
    current_frame.quan_label.configure(text=str(get_quantity(menu_item)), fg='#007FFF')
    current_frame.quan_label.pack(side=LEFT, padx=12)

    #Create increment and decrement buttons for every food item
    current_frame.add_bttn.configure(text='+', bg='green', fg='white', command=add_btn_click)
    current_frame.minus_bttn.configure(text='-', bg='red', fg='white', command=minus_btn_click)
    current_frame.add_bttn.pack(side=LEFT, padx=5)
    current_frame.minus_bttn.pack(side=LEFT, padx=5)

    #Add each frame to the root window
for row in menu_gui_dict:
    menu_gui_dict.get(row).pack(padx=20, pady=5)

#execute gui
root.mainloop()
#print(menu_gui_dict)