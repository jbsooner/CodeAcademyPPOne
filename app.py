import pandas as pd
from tabulate import tabulate
import datetime

df = pd.read_csv('insurance.csv')

# tabulet table format
tabul_format = 'pretty'  # https://pypi.org/project/tabulate/ -- go here for different table formats

print('The current data and time is: ', datetime.datetime.now())
print('===============================================================================================================')
print('Global Data')

# Getting general data from the dataset
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
print('===============================================================================================================')

print('===============================================================================================================')

results_dict = {}

# This function will allow us to get stats for any column value we want for example are they a smoker
def sort_by_col(column, value):
    data_col = column
    value_to_lookup = value
    # print('Global', value.capitalize(), 'Data')
    if data_col == 'age':
        print('Global', data_col.capitalize(), 'Data')
        dict_key = 'Global {} Data'.format(data_col.capitalize())
    elif data_col == 'sex' and value_to_lookup == 'female':
        print('Global Female Data')
        dict_key = 'Global Female Data'
    elif data_col == 'sex' and value_to_lookup == 'male':
        print('Global Male Data')
        dict_key = 'Global Male Data'
    elif data_col == 'children':
        print('Number of Children', value_to_lookup)
        dict_key = 'Number of Children {}'.format(value_to_lookup)
    elif data_col == 'smoker' and value_to_lookup == 'yes':
        print('Is a Smoker')
        dict_key = 'Is a Smoker'
    elif data_col == 'smoker' and value_to_lookup == 'no':
        print('Is not a Smoker')
        dict_key = 'Is not a Smoker'
    elif data_col == 'region':
        print('Global', value_to_lookup.capitalize(), 'Data')
        dict_key = 'Global {} Data'.format(value_to_lookup.capitalize())
    elif data_col == 'charges':
        print('Global Charges Data')
        dict_key = 'Global Charges Data'

    # Create a DataFrame for the item we want to inspect.
    new_df = df[(df[data_col] == value_to_lookup)]


# Create a global_list for the variables below to be appended to / created a header list for the tablulate table
    list_item = []
    header_list_global_smoker = ['Avg Age', 'Total Items', 'Total Smokers',
                             'Total Insurance Costs', 'Total BMI', 'Total Avg Costs', 'Total Avg BMI']

    # Get my variables to be appended to the global_list
    age_mean = round(new_df['age'].mean())
    items_total = new_df['region'].count()
    smoker_item_total = sum(new_df['smoker'] == 'yes')
    item_total_cost = round(new_df['charges'].sum(), 2)
    item_bmi_total = round(new_df['bmi'].sum(), 2)
    item_avg_cost = round((item_total_cost / items_total), 2)
    item_avg_bmi = round((item_bmi_total / items_total), 2)

    # Append my global variables to the global_list
    list_item.append(age_mean)
    list_item.append(items_total)
    list_item.append(smoker_item_total)
    list_item.append(item_total_cost)
    list_item.append(item_bmi_total)
    list_item.append(item_avg_cost)
    list_item.append(item_avg_bmi)

    # Had to make this so I could use tabulate for a single item list / had to create a list of lists
    tabulate_end_list_smoker = ['x', 'x', 'x', 'x', 'x', 'x', 'x']
    # Create a empty list to append the global list / tabulate_end_list to create the tabulate table
    tabulate_list = []
    tabulate_list.append(list_item)
    tabulate_list.append(tabulate_end_list_smoker)
    
    data_dict = {dict_key:[age_mean, items_total, smoker_item_total, item_total_cost, item_bmi_total, item_avg_cost, item_avg_bmi]}
    results_dict.update(data_dict)

    # print out the tabulate table
    print(tabulate(tabulate_list, headers=header_list_global_smoker, tablefmt=tabul_format, floatfmt='.2f'))
    print('===============================================================================================================')
    

sort_by_col('region', 'southwest')
sort_by_col('region', 'northwest')
sort_by_col('sex', 'female')
sort_by_col('sex', 'male')
sort_by_col('children',3)
