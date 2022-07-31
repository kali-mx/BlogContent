#!/usr/bin/python3
# a simple data entry program that calculates truck fuel tax by state, storing data to disk in comma separated values (csv)
import subprocess,csv,os.path,os
from functools import update_wrapper
from typing import Any
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from art import tprint

subprocess.call('clear', shell=True)   ##clear screen##

states_db = {'MN':.04, 'WI':.05, 'CO':.06, 'NJ':.09}
mpg = fuel_cost = start_mileage = end_mileage = 0

tprint('Trucker_Count',font='smooth1')
print('authored by: Thomas Ahartz\n')
print('*'*40, '\n')

def sanitised(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError('min_ must be less than or equal to max_.')
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print('Input type must be {0}.'.format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print('Input must be less than or equal to {0}.'.format(max_))
        elif min_ is not None and ui < min_:
            print('Input must be greater than or equal to {0}.'.format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = 'Input must be between {0.start} and {0.stop}.'
                print(template.format(range_))
            else:
                template = 'Input must be {0}.'
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = ' or '.join((
                        ', '.join(str(x) for x in range_[:-1]),
                         str(range_[-1])
                    ))
                    print(template.format(expected))
        elif type_ is str and ui.upper() not in states_db:
            print('Not in state database')     
            continue       
        else:
            return ui




def enter_trip():
    while True:
        trip = 1
        truck_number = sanitised('Enter Truck #: ', int, 1, 99999)
        fuel_cost = sanitised('Enter fuel:$ ', float, 1, 9999)
        fuel_gallons = sanitised('Enter gallons: ', float, 1, 9999)
        start_mileage = sanitised('Enter trip mileage start: ', float, 1, 5000000)
        end_mileage = sanitised('Enter trip mileage end: ', float, start_mileage, 5000000)
        state_of_travel = sanitised('State traveled: ', str)
        trip_mileage = (end_mileage - start_mileage)
        
        mpg = trip_mileage / fuel_gallons
        print('mpg:', '{:.2f}'.format(mpg))
        tax_rate = ([(k, states_db[k]) for k in states_db if state_of_travel.upper() == k])
        fuel_tax = tax_rate[0][1] * trip_mileage
        print('fuel tax:$', '{:.2f}'.format(fuel_tax))
        print('truck number:', truck_number, 'fuel_cost', fuel_cost, 'start_mileage', start_mileage)
        trip += 1
        
        fields = ['truck_number', 'fuel_cost', 'fuel_gal', 'start_mileage', 'end_mileage', 'trip_mileage', 'state', 'tax_rate', 'fuel_tax']
        if os.path.exists('data.txt') == False:
            with open('data.txt', 'w') as f:  
                # creating a csv writer object  
                csvwriter = csv.writer(f)  
                # writing the fields  
                csvwriter.writerow(fields)
                f.close()

        rows = [str(truck_number), str(fuel_cost), str(fuel_gallons), str(start_mileage), str(end_mileage), str(trip_mileage), state_of_travel, str(tax_rate[0][1]), str(fuel_tax)] # data row
        # writing to csv file  
        with open('data.txt', 'a') as f:  
            # creating a csv writer object  
            csvwriter = csv.writer(f, delimiter = ',')  
            # writing the data rows  
            csvwriter.writerow(rows)
        f.close()
        main()


def reports():

    data = pd.read_csv('data.txt')
    print(data,'\n')
    sumfuel = data.groupby(['truck_number'])['fuel_tax', 'fuel_cost', 'trip_mileage'].agg('sum').reset_index()
    sumfuel = sumfuel.to_string(header=False,index=None)
    print('\n\n\t***TOTALS***')
    print('truck  taxes  gals  miles')
    print(sumfuel, '\n'*3)
    
    #syntax souveniers:
    #with open('data.txt', 'r') as f:
    #df1 = ((data['end_mileage'] - data['start_mileage']) * .05).to_frame('col')
    #result = df.groupby('Courses')['Fee','Discount'].aggregate('sum')
    #sumfuel = data.groupby(['truck_number'])['fuel_tax'].sum()


def main():
    
    print('[1] Enter Trip\n[2] Reporting\n[3] Edit Data\n','\nCtrl-C to exit\n\n')
    print('*'*40, '\n')
    option = sanitised('Select Menu Option:', int, 1, 3)
    if option == 1:
        enter_trip()
        main()
    elif option == 2:
        reports()
        main()
    else:
        print('Opening nano...\n') 
        os.system('nano data.txt')       
        main()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        quit()
