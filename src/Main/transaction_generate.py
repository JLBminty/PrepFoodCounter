"""
+Generate a new Transactions.csv file every x time
+Will contain random amounts of prep food items (0-n)
+The created file will be read by the main program
+This program should be standalone
+Each generation will be saved to a larger file that keeps track of inputs for the duration of the programs run
+Format of the form: orderNum,orderName,orderType,orderTotal,orderItems
"""
import random
import csv

# Tracks current order number
current_order_num = 0
# List of names an order can have
names = ["Mae","Jimmy","David","Dean","Thomas","Sean","Gus","Jesse","Naya","Zechariah","Zyla","Darian","Jolie","Salvatore","Leanna","Jericho","Yamileth","Mitchell","Alistair","Elisabeth","Calum","Ensley","Van","Ashlyn","Zev","Allison","Langston","August","Mccoy","Kimber","Ulises","Marleigh","Lucien","Soraya","Benedict","Anaiah","Carlos","Analeia","Coleson","Waverly","Meir","Yasmin","Henrik","Zora","Jiraiya","Joelle","Kellan","Lilia","Alfonso","Nancy","Azai","Campbell","Indigo","Kylen","Harely","Felipe","Laylani","Leif","Romy","Scout","Curtis","Ayra","Amir","Giovanna","Kiaan","Siya","Maurice","Katelyn","Krue","Madalyn","Shimon","Natasha","Zyon","Alaiya","Damari","Honey","Jairo","Khalid","Sarahi","Kabir","Elsa","Jireh","Emmeline","Mathew","Hadlee","Lilianna","Eddie","Ainhoa","Arden","Elliot","Cedric","Jazmine","Nazir","Aadhya","Alessio","Guinevere","Khai","Rayne","Marcellus","Clair","Wesson","Saanvi","Yisroel","Zymir","Salome","Landen","Tilly","Darren","Yusra","Legacy","Akira","Devon","Henley","Judson","Lyanna","Vihaan","Quincy","Yitzchok","Rosalee","Zen","Dangelo","Ainara","Adler","Annika","Aspen","Ayah","Brodie","Violette","Kase","Aleia","Khaza","Mazie","Dash","Amyra","Makari","Selena","Neo","Zavier","Paloma","Evren","Elouise","Imran","Etta","Julietta","Cain","Kamiyah","Ira","Zoya","Osiris","Jayleen","Kassidy","Yaakov","Keily","Ephraim","Harlee","Kiera","Wallace","Liberty","Yeshua","Darcy","Kannon","Dior","Kingsley","Lisa","Noah","Malika","Arisbeth","Ermias","Kara","Harold","Bailee","Joziah","Elani","Rene","Harmoni","Truce","Mariella","Aldo","Zayla","Dimitri","Emi","Halo","Jianna","Ronnie","Maelynn","Vance","Avani","Lavender","Ishaan","Karter","Kace","Raina","Stefan"]
    #https://github.com/aruljohn/popular-baby-names/tree/master/2024
# List of types of orders
types = ["Carryout","Curbside","DD","Dine-in","Drive-Thru","Mobile-Carryout","Mobile-Thru"]
# Dictionary of menu-items and thier prices
menu = {
    "CFA":5.45,
    "CFASpicy":5.75,
    "CFADlx":6.15,
    "CFASpicyDlx":6.45,
    "5Nugg":3.45,
    "8Nugg":5.49,
    "12Nugg":7.49,
    "CobbSld":9.95,
    "CobbSld*":9.95,
    "SWSld":10.15,
    "SWSld*":10.15,
    "MrktSld":10.15,
    "MrktSld*":10.15,
    "Wrap":8.65,

    "SmFry":2.45,
    "MedFry":2.75,
    "LgFry":3.15,
    "SmFruit":3.29,
    "MedFruit":4.39,
    "LgFruit":6.35,
    "KaleSld":4.39,
    "SideSld":4.39,
    "Prft":4.99,

    "SmDrink":1.99,
    "MedDrink":2.49,
    "LgDrink":2.89,
    "Shke":4.95
    }

def generate_order():
    """
    Generate the list that will become a row in the csv
    """
    order = ['orderNum','orderName','orderType','orderTotal','orderItems']
    order[0] = current_order_num
    order[1] = names[pick_random_num(0, len(names)-1)]
    order[2] = types[pick_random_num(0, len(types)-1)]
    
    # Determine number of items in order sum their prices for last 2 columns
    order_items_list = [""]*pick_random_num(1,18)
    order_items_string = ""
    for i in range(len(order_items_list)):
        order_items_list[i] = list(menu)[pick_random_num(0,len(menu)-1)]
        order_items_string += (order_items_list[i]+"|")
    #print(order_items_list)
    order_total = 0
    for item in order_items_list:
        order_total += menu.get(item)
    order[3]=order_total
    order[4]=order_items_string    
    
    #print(order)
    return order

def generate_data():
    """
    Generate all the data for the new .csv
    """
    data = [
        ['orderNum','orderName','orderType','orderTotal','orderItems']
    ]
    # generate more data
    total_orders = pick_random_num(1,20)
    for i in range(0,total_orders):
        data.append(generate_order())
        global current_order_num
        current_order_num += 1
    
    return data

def generate_csv(data:list):
    """
    Generate the new Transactions.csv
    Formatted: orderNum,orderName,orderType,orderTotal,orderItems
    """
    csv_file_path = 'src\Data\Orders.csv'
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def pick_random_num(min:int, max:int):
    """
    Random number picker for: 
        choosing number of orders.
        and choosing number of items in a order.
    """
    num = random.randint(min, max)
    return num

# Main operation
def transaction_generate_main():
    generate_csv(generate_data())
#    print("New file generated!")