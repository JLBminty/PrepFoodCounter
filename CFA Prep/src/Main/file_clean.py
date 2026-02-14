import pandas as pd
from prep_menu import prep_menu_abbrs as menu

    # Load transaction data from CSV into pandas DataFrame
file_path = r"C:\Users\j1012\Desktop\Python\CFA Prep\src\Data\Transactions.csv" 
df = pd.read_csv(file_path, encoding='utf-8', usecols=['orderItems'])
#print(df)    
    # Remove empty rows in the DataFrame
df.dropna(inplace=True)

food=df.values.tolist()
    # Split rows by comma for individual items
split_data = []
for row in food:
    #print(row)
    for item in row:
        lista=item.split('|')
        for a in lista:
            split_data.append(a)

    # Remove remaining irrelvant orders
#print(split_data)
#print("menu",menu)

for i in range(len(split_data)):
    #print(split_data[i])
    if split_data[i] not in menu:
        split_data[i] = ""
    #print(split_data[i])


clean_data = [a for a in split_data if a]
    #https://www.geeksforgeeks.org/python/python-list-comprehension/
    #https://www.geeksforgeeks.org/python/python-remove-empty-list-from-list/
#print(clean_data)

#function that will return the cleaned data when called
def export_data():
    return clean_data
