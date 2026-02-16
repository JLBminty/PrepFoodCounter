
    #List of items offered on the menu
prep_menu_items = []
    #list of all relevant abbreviations
prep_menu_abbrs = []
    #dictionary linking abbriviation to object name
prep_menu_dict = {}

class MenuItem():
    quantity=0
    name=""
    abbr=""

    def __init__(self,name:str,abbr:str):
        """Initialize menu items on program start as 0
        Add menu item's abbreviation-property(abbr) value(string) to the menu list
        Add menu item's increment function call to the menu dictionary"""
        self.quantity = 0
        self.name = name
        self.abbr = abbr
        prep_menu_items.append(self)
        prep_menu_abbrs.append(self.abbr)



def add_quantity(self:MenuItem, add:int, neg_flag:bool):
    """Crement how many of an item are available 
    Should raise exception if quantity is going negative
    and set quantity to 0
    Returns the new quantity value"""
    try:
        if neg_flag:
            new_quantity = self.quantity - add
        else:
            new_quantity = self.quantity + add
    except(new_quantity<0):
        new_quantity = 0
    self.quantity = new_quantity

def set_quantity(self:MenuItem, value:int):
    """Overwrite the quantity of item available
    Should raise exception if entered value is negative
    and set quantity to 0"""
    try:
        new_quantity = value
    except(new_quantity<0):
        print("Cannot be negative, setting quantity to 0")
        new_quantity = 0
    self.quantity = new_quantity

def get_quantity(self:MenuItem):
    """Return the quantity of item available"""
    return self.quantity

def get_name(self:MenuItem):
    """Return the proper-name of the food item"""
    return self.name


def update_prep_stock(orders):
    print(orders)
    for item in orders:
        add_quantity(prep_menu_dict.get(item, lambda: "unknown"), 1, False)
    for item in prep_menu_items:
        print(item.name, ": ", item.quantity)
    print("Stock updated successfully")
    return prep_menu_dict


#initialize all prep objects on the menu and add them to the menu dictionary
CobbSld = MenuItem("Cobb Salad", "CobbSld")
prep_menu_dict.update({CobbSld.abbr:CobbSld})
Wrap = MenuItem("Cool Wrap", "Wrap")
prep_menu_dict.update({Wrap.abbr:Wrap})
SmFruit = MenuItem("Small Fruit Cup", "SmFruit")
prep_menu_dict.update({SmFruit.abbr:SmFruit})
MedFruit = MenuItem("Medium Fruit Cup", "MedFruit")
prep_menu_dict.update({MedFruit.abbr:MedFruit})
LgFruit = MenuItem("Large Fruit Cup", "LgFruit")
prep_menu_dict.update({LgFruit.abbr:LgFruit})
KaleSld = MenuItem("Kale Crunch Side", "KaleSld")
prep_menu_dict.update({KaleSld.abbr:KaleSld})
MrktSld = MenuItem("Market Salad", "MrktSld")
prep_menu_dict.update({MrktSld.abbr:MrktSld})
Prft = MenuItem("Parfait", "Prft")
prep_menu_dict.update({Prft.abbr:Prft})
SideSld = MenuItem("Side Salad", "SideSld")
prep_menu_dict.update({SideSld.abbr:SideSld})
SWSld = MenuItem("Spicy Southwest Salad", "SWSld")
prep_menu_dict.update({SWSld.abbr:SWSld})

#print(prep_menu_list)