import pandas as pd
from tabulate import tabulate

# 1. Find the average age across all data points -- done
# 2. Find the average insurance cost across all data points -- done
# 3. Find how many items in each region -- done
# 4. Find average age and cost across each region -- done

# Create our dataframe from the file        
df = pd.read_csv('insurance.csv')

global_list = []
header_list_global = ['Avg Age', 'Total Items', 'Total Smokers', 'Total Insurance Costs', 'Total BMI', 'Total Avg Costs', 'Total Avg BMI']

total_age_mean = round(df['age'].mean())
total_items = df['region'].count()
total_smokers = sum(df['smoker'] == 'yes')
total_insurance_costs_global = round(df['charges'].sum(),2)
total_bmi_global = round(df['bmi'].sum(), 2)
total_avg_cost = round((total_insurance_costs_global / total_items),2)
total_avg_bmi = round((total_bmi_global / total_items),2)

global_list.append(total_age_mean)
global_list.append(total_items)
global_list.append(total_smokers)
global_list.append(total_insurance_costs_global)
global_list.append(total_bmi_global)
global_list.append(total_avg_cost)
global_list.append(total_avg_bmi)

# Had to make this so I could use tabulate for a single item list / had to create a list of lists
tabulate_end_list = ['x', 'x', 'x', 'x', 'x', 'x', 'x']
global_list_total = []
global_list_total.append(global_list)
global_list_total.append(tabulate_end_list)


print(tabulate(global_list_total, headers=header_list_global, tablefmt='orgtbl'))

print('\n')
print('=======================================================================================================================')
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

print(tabulate(total_list, headers=header_list, tablefmt='orgtbl'))
