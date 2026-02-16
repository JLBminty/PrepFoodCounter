import time
import prep_menu
from prep_menu import update_prep_stock
import file_clean
from file_clean import export_data
import gui_main
from gui_main import update_stock_labels

"""
https://www.geeksforgeeks.org/python/python-time-module/
https://docs.python.org/3/library/time.html#functions
"""


#initialize prep_menu and the list of abbreviations
prep_menu
gui_main
#get the current time: start the 'timer': 1 minute
try:
    current_time = time.localtime()
except(OverflowError):
    current_time = time.time()
    
    #start the clock loop
#get file data
file_clean
#update counts and user messages for GUI
update_stock_labels(update_prep_stock(export_data()))
    #repeat

#include options for overriding counts
