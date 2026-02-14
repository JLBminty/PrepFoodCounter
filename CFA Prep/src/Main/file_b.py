import csv
from prep_menu import prep_menu_abbrs as menu

print(menu)
file_path = r"C:\Users\j1012\Desktop\Python\CFA Prep\src\Data\Transactions.csv"
with open(file_path, newline='', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, quotechar='"')
    for row in file_reader:
        print(', '.join(row))