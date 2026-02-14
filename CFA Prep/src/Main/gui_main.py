from tkinter import *
from datetime import datetime

from prep_menu import prep_menu_dict, MenuItem, add_quantity, get_quantity, set_quantity, get_name

#dictionary linking menu objects to a row in GUI
menu_gui_dict = {}

#crement buttons code
def btn_click(btn_funct:str,item:MenuItem):
    pass

#scrollbar code
def scroll():
    pass

#user interface script
root = Tk()
root.title("Prep Food Counter")
root.geometry('800x600')
root.configure(bg='gray')

scroll_bar = Scrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)
"""PhotoImage for images in PGM, PPM, GIF and PNG formats. """
    #Root window title label
title = Label(root, text='Prep Stock', fg='#007FFF')
title.pack()
    #Lastest update time label
latest_update = Label(root, text=datetime.now().strftime("%d-%m-%Y | %H:%M"), fg='#007FFF')
latest_update.pack()
    #Rows of frames for each menu item
for row in prep_menu_dict:
    menu_gui_dict.update({prep_menu_dict.get(row):Frame(root, bg="#CCE5FF", bd=2, width=750, height=120)})

    #Fill the created frames with all thier components
for frame in menu_gui_dict:
    #picture on the left
#    print(type(frame))
    #name of the food
    food_name = Label(menu_gui_dict.get(frame), text=get_name(frame), fg='#007FFF')
    food_name.pack(padx=20)
    #number of food available
    food_quan = Label(menu_gui_dict.get(frame), text=str(get_quantity(frame)), fg='#007FFF')
    food_quan.pack(padx=10)
    #Create increment and decrement buttons for every food item
    increment_btn = Button(menu_gui_dict.get(frame), text='+', bg='green', fg='white', command=btn_click("+",prep_menu_dict.get(row)))
    decrement_btn = Button(menu_gui_dict.get(frame), text='-', bg='red', fg='white', command=btn_click("-",prep_menu_dict.get(row)))
    increment_btn.pack(padx=30)
    decrement_btn.pack(padx=30)
    pass

    #Add each frame to the root window
for row in menu_gui_dict:
    menu_gui_dict.get(row).pack(padx=20, pady=5)

#execute gui
root.mainloop()
#print(menu_gui_dict)