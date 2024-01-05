import Numerial_analysis
from Numerical_analysis import *

print('Welcome to our automated analysis')

inp = input('Input the location of the file that you want to analize')

print(inp)



data = pd.read_csv(inp)

data.head()


print(data.columns)

Number_of_columns = int(input('How many columns do you want to work on:'))

columns_names = []

for i in range(Number_of_columns):
    data_column = input('Which column do you want to work on:')
    columns_names.append(data_column)

selected_data = data[columns_names]
print(selected_data.head())


print("What operation do you want to perform in the column's?")
inp = input('What would you like to do:')
data = inp.lower()

if data in ['perform mathematical analysis', 'perform numerical analysis']:
    inp = input('What kind of analysis:')
    reply = inp.lower()

    from 