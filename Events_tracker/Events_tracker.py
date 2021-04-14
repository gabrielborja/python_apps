#Python program designed to register events versus time

#Import necessary packages to handle date, time and output format
from datetime import datetime
import time
import csv

#Function used to register events from the user
def register_events():
    """function used to register events from the user with the corresponding datetime"""
    val = input('\nEnter your observation: ')
    return (check_time(), val)

#Function that returns the current date and time with milliseconds precision
def check_time():
    """function used to return a datetime object with milliseconds precision"""
    return str(datetime.now())[:-3]#.strftime('%m/%d/%Y %I:%M:%S.%f %p')

#Function used to update a dictionary with a tuple of datetime and its corresponding value
def update_dict(my_dict, my_tuple):
    """function used to update a dictionary with a tuple of datetime and its corresponding value"""
    my_dict.update({my_tuple[0]: my_tuple[1]})

#Function that saves the final dictionary to csv file appending the current date and file name
def f_saver(my_dict, process_name):
    """function used to save the final dictionary to a csv file in the hard drive,
    appending the current date and process name to the name of the file"""
    csv_columns = ['Time','Num']
    time_str = check_time()[:10] #Slicing the first 10 char to append the current date and file name.
    with open(f'{time_str}_{process_name}.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([i for i in csv_columns]) #Writing the column headers at the top of the csv file
        for k, v in my_dict.items():
            writer.writerow([k, v]) #Writing all key and values to the csv file
    print('\nThe file was saved...')

#Main program used to run during the measurement period
def event_tracker():
    """ Python Program used to track and register events versus time."""
    my_data = {}
    
    print('\nWelcome to the program to register time events.')
    my_process = input('\nWhat process do you want to track today: ').capitalize().strip()
  
    try:
        while True:
            update_dict(my_data, register_events()) #Capture events vs. time
    except KeyboardInterrupt: #==> Interrupt the program by pressing Ctrl + C
        #Catch the exception and call the f_saver function to saved the data to a csv file.
        f_saver(my_data, my_process)
    print('\nThe program finished\n')

if __name__ == '__main__': event_tracker()