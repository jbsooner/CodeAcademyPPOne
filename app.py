import pandas as pd
from tabulate import tabulate
import datetime
import numpy as np


print('The current data and time is: ', datetime.datetime.now())
print('\n')
print('==============================================================================================================================')
print('Global Data')

tabul_format = 'pretty'  # https://pypi.org/project/tabulate/ -- go here for different table formats

# Create our dataframe from the file        
df = pd.read_csv('insurance.csv')


# Create a global_list for the variables below to be appended to / created a header list for the tablulate table
global_list = []
header_list_global = ['Avg Age', 'Total Items', 'Total Smokers', 'Total Insurance Costs', 'Total BMI', 'Total Avg Costs', 'Total Avg BMI']

# Get my variables to be appended to the global_list
total_age_mean = round(df['age'].mean())
total_items = df['region'].count()
total_smokers = sum(df['smoker'] == 'yes')
total_insurance_costs_global = round(df['charges'].sum(),2)
total_bmi_global = round(df['bmi'].sum(), 2)
total_avg_cost = round((total_insurance_costs_global / total_items),2)
total_avg_bmi = round((total_bmi_global / total_items),2)

# Append my global variables to the global_list
global_list.append(total_age_mean)
global_list.append(total_items)
global_list.append(total_smokers)
global_list.append(total_insurance_costs_global)
global_list.append(total_bmi_global)
global_list.append(total_avg_cost)
global_list.append(total_avg_bmi)

# Had to make this so I could use tabulate for a single item list / had to create a list of lists
tabulate_end_list = ['x', 'x', 'x', 'x', 'x', 'x', 'x']
# Create a empty list to append the global list / tabulate_end_list to create the tabulate table
global_list_total = []
global_list_total.append(global_list)
global_list_total.append(tabulate_end_list)

# print out the tabulate table
print(tabulate(global_list_total, headers=header_list_global, tablefmt=tabul_format, floatfmt='.2f'))
print('==============================================================================================================================')

print('\n')
print('==============================================================================================================================')
print('Data by Region')

# Get the average of a column
def average(item):
    average_item = df[item].mean()
    return round(average_item)

region_dict = {}


def region_count(items):
    for val, cnt in df[items].value_counts().iteritems():
        region_dict[val] = cnt
    return region_dict



def region_data(which_region):
    current_region = df[df['region'].isin([which_region])]
    current_region_mean_age = round(current_region['age'].mean())
    current_region_count = current_region['region'].count()
    smoker_count = current_region['smoker'] == 'yes'
    total_insurance_costs = current_region['charges'].sum()
    total_bmi = current_region['bmi'].sum()
    average_cost_region = total_insurance_costs / current_region_count
    average_bmi = total_bmi / current_region_count
    
    
    return which_region, current_region_mean_age, current_region_count, sum(smoker_count), round(total_insurance_costs), round(average_cost_region), round(average_bmi, 2)


region_count('region')

header_list = ['Region', 'Avg Age', 'Region Count', 'Smoker Count', 'Total Insurance Cost', 'Avg Cost', 'Avg BMI']

total_list = []
for key in region_dict.keys():
    region_data(key)
    # print('The {} region has an average age of {}, count of {}, {} smokers, {} total insurance costs, average cost of {}, and average bmi of {}'.format(key, region_data(key)[1], region_data(key)[2], region_data(key)[3], region_data(key)[4], region_data(key)[5], region_data(key)[6]))
    new_list = []
    new_list.append(key)
    new_list.append(region_data(key)[1])
    new_list.append(region_data(key)[2])
    new_list.append(region_data(key)[3])
    new_list.append(region_data(key)[4])
    new_list.append(region_data(key)[5])
    new_list.append(region_data(key)[6])
    total_list.append(new_list)

print(tabulate(total_list, headers=header_list, tablefmt=tabul_format, floatfmt='.2f'))
print('==============================================================================================================================')
print('Global Smoker Data')

# Create a smoker only dataframe
smoker_df = df[(df.smoker == 'yes')]


# Create a global_list for the variables below to be appended to / created a header list for the tablulate table
global_list_smoker = []
header_list_global_smoker = ['Avg Age', 'Total Items', 'Total Smokers', 'Total Insurance Costs', 'Total BMI', 'Total Avg Costs', 'Total Avg BMI']

# Get my variables to be appended to the global_list
total_age_mean_smoker = round(smoker_df['age'].mean())
total_items_smoker = smoker_df['region'].count()
total_smokers_smoker = sum(smoker_df['smoker'] == 'yes')
total_insurance_costs_global_smoker = round(smoker_df['charges'].sum(), 2)
total_bmi_global_smoker = round(smoker_df['bmi'].sum(), 2)
total_avg_cost_smoker = round((total_insurance_costs_global_smoker / total_items_smoker), 2)
total_avg_bmi_smoker = round((total_bmi_global_smoker / total_items_smoker), 2)

# Append my global variables to the global_list
global_list_smoker.append(total_age_mean_smoker)
global_list_smoker.append(total_items_smoker)
global_list_smoker.append(total_smokers_smoker)
global_list_smoker.append(total_insurance_costs_global_smoker)
global_list_smoker.append(total_bmi_global_smoker)
global_list_smoker.append(total_avg_cost_smoker)
global_list_smoker.append(total_avg_bmi_smoker)

# Had to make this so I could use tabulate for a single item list / had to create a list of lists
tabulate_end_list_smoker = ['x', 'x', 'x', 'x', 'x', 'x', 'x']
# Create a empty list to append the global list / tabulate_end_list to create the tabulate table
global_list_total_smoker = []
global_list_total_smoker.append(global_list_smoker)
global_list_total_smoker.append(tabulate_end_list_smoker)

# print out the tabulate table
print(tabulate(global_list_total_smoker, headers=header_list_global_smoker, tablefmt=tabul_format, floatfmt='.2f'))
print('==============================================================================================================================')

print('\n')

percent_smokers = round((total_items_smoker / total_items)*100, 2)
price_diff = round(total_avg_cost_smoker - total_avg_cost)
print('==============================================================================================================================')
print('{}% of the data set are smokers.'.format(percent_smokers))
print('If you smoke your insurance is on average {} higher than a non-smoker.'.format(price_diff))
print('The southeast has the highest average cost, average bmi, smokers, and total insurance cost.')
print('The northeast has the second highest average cost due to having the second largest group of smokers.')
print('The average age across all of the data is 39.')
print('==============================================================================================================================')
print('\n')
