# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Ruikai Li for COMP9021


import sys
import os
import csv
import re


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

L = []
month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
year_range = year_or_range_of_years.split('--')
if len(year_range) == 1:
    year_range.append(year_range[0])
with open(filename) as file:
    for line in file:
        source_name, _, _ = line.split(',')
        _, date, _ = line.split(',')
        _, _, mean = line.split(',')
        if date != 'Date':
            year = date.split('-')[0]
            month1 = date.split('-')[1]
        if source_name == source:
            if int(year_range[0]) <= int(year_range[1]):
                if int(year) >= int(year_range[0]) and int(year) <= int(year_range[1]):
                    if month1 == month_dict[month]:
                        L.append(line)
            elif int(year_range[0]) >= int(year_range[1]):
                if int(year) <= int(year_range[0]) and int(year) >= int(year_range[1]):
                    if month1 == month_dict[month]:
                        L.append(line)

mean_list = []
years_above_average = []
for i in L:
    i = re.sub('\n', ',', i)
    answer_list = i.split(',')
    mean_list.append(float(answer_list[2]))
average = sum(mean_list) / len(L)
for i in L:
    i = re.sub('\n', ',', i)
    answer_list = i.split(',')
    if float(answer_list[2]) > average:
        years_above_average.append(int(answer_list[1][0:4]))

years_above_average = sorted(years_above_average)


print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)