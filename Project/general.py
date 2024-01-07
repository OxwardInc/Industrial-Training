# main_script.py
import numpy as np
import pandas as pd
from Numerical_analysis import one_column_analysis, more_than_one_column

# Welcome message
print('Welcome to our automated analysis')

# Getting the file for the analysis
inp = input('Input the location of the file that you want to analyze: ')
data = pd.read_csv(inp)

print(data.columns)

# Getting the number of columns from the user
Number_of_columns = int(input('How many columns do you want to work on: '))

columns_names = []

for i in range(Number_of_columns):
    data_column = input('Which column do you want to work on: ')
    columns_names.append(data_column)

selected_data = data[columns_names]
print(selected_data.head())

print("What operation do you want to perform in the columns?")
inp = input('What would you like to do: ')
data = inp.lower()

if data in ['perform mathematical analysis', 'perform numerical analysis']:
    inp = input('What kind of analysis: ')
    reply = inp.lower()

    if len(columns_names) == 1:
        one_column_analysis(selected_data[columns_names[0]], reply, columns_names)
    else:
        more_than_one_column(selected_data, columns_names)

# Assuming you want to print the head of 'selected_data'
print(selected_data.head())
