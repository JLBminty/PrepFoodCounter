from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

from prep_menu import prep_menu_dict, MenuItem, add_quantity, get_quantity, set_quantity, get_name, get_path

#dictionary linking menu objects to a row in GUI
menu_gui_dict = {}
#dictionary of photoimage items used by menu items
menu_images = {}

#crement buttons code: manual stock updates
def btn_click(btn_funct:str,item:MenuItem):
    pass

#automatic stock updates
def update_stock_labels(items:dict):
    for item in menu_gui_dict:
        new_quan = get_quantity(item)
        menu_gui_dict.get(item).food_quan.configure(text=new_quan)
    root.update()
    pass

#user interface script
root = Tk()
root.title("Prep Food Counter")
root.geometry('800x600')
root.maxsize(800,600)

    #scrollable canvas
canvas = Canvas(root, bg='gray')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

    #scrollbar
scroll_bar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scroll_bar.set)
canvas.bind("<Configure>",lambda e: canvas.config(scrollregion= canvas.bbox(ALL)))

main_frame = Frame(canvas, bg='black')
#main_frame.pack(fill=BOTH, expand=True)
canvas.create_window((0,0),window=main_frame, anchor='n')

    #Root window title label
title = Label(main_frame, text='Prep Stock', fg='#007FFF')
title.pack()

    #Lastest update time label
latest_update = Label(main_frame, text=datetime.now().strftime("%d-%m-%Y | %H:%M"), fg='#007FFF')
latest_update.pack()

    #Row frames for each menu item
for row in prep_menu_dict:  
    menu_gui_dict.update({prep_menu_dict.get(row):Frame(main_frame, bg="#CCE5FF", bd=2, width=780, height=120)})

    #Reference to Image objects for each row
for row in menu_gui_dict:
#    print(type(row))
    temp_img = Image.open(get_path(row))
    resize = temp_img.resize((100, 100))
    tk_img = ImageTk.PhotoImage(resize)
    menu_images.update({row:tk_img})

#print(menu_images)

    #Fill the created frames with all thier components: pack frames horizontally
for frame in menu_gui_dict:
#    print(type(frame))
    #picture on the left
    img = menu_images.get(frame)
#    print(type(img))
    food_image = Label(menu_gui_dict.get(frame), image=img)
    food_image.image = img
#    print(type(menu_images.get(get_path(frame))))
    food_image.pack(side=LEFT, padx=4)
#    print(type(frame))
    #name of the food
    food_name = Label(menu_gui_dict.get(frame), text=get_name(frame), fg='#007FFF')
    food_name.pack(side=LEFT, padx=10)
    #number of food available
    food_quan = Label(menu_gui_dict.get(frame), text=str(get_quantity(frame)), fg='#007FFF')
    food_quan.pack(side=LEFT, padx=12)
    #Create increment and decrement buttons for every food item
    increment_btn = Button(menu_gui_dict.get(frame), text='+', bg='green', fg='white', command=btn_click("+",prep_menu_dict.get(row)))
    decrement_btn = Button(menu_gui_dict.get(frame), text='-', bg='red', fg='white', command=btn_click("-",prep_menu_dict.get(row)))
    increment_btn.pack(side=LEFT, padx=5)
    decrement_btn.pack(side=LEFT, padx=5)
    pass

    #Add each frame to the root window
for row in menu_gui_dict:
    menu_gui_dict.get(row).pack(padx=20, pady=5)

#execute gui
root.mainloop()
#print(menu_gui_dict)