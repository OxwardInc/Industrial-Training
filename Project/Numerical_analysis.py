import numpy as np
import pandas as pd


# Check if 'selected_data' is not numeric and convert if needed
if not isinstance(selected_data, (int, float)):
    selected_data = pd.to_numeric(selected_data, errors='coerce')

# Check the length of columns only once
length_of_columns = len(columns_names)
if length_of_columns == 1:
    # Asking if they'll like to analyse based on any condition
    cond = input('Do you want to apply a specific condition or just take it as is?').lower()
    if cond == 'no':
        # Perform the selected analysis
        if reply == 'find the sum of data' or reply == 'find the sum':
            result = np.sum(selected_data)

        elif reply in ['find the min of data', 'find the min']:
            result = np.min(selected_data)

        elif reply in ['find the max of data', 'find the max']:
            result = np.max(selected_data)

        elif reply in ['find the standard deviation of data', 'find the std']:
            result = np.std(selected_data)

        elif reply in ['find the mean of data', 'find the mean']:
            result = np.mean(selected_data)

        elif reply in ['find the median of data', 'find the median']:
            result = np.median(selected_data)

        elif reply in ['find the variance value of data', 'find the variance']:
            result = np.var(selected_data)
    
        elif reply in ['find percentile value']:
            num_of_percentile = int(input('Enter the number of percentile:'))
            result = np.percentile(selected_data,num_of_percentile)
        
        elif reply in ['find the cumulative sum']:
            result = np.cumsum(selected_data)

        elif reply in ['find the unique value']:
            result = np.unique(selected_data)

        else:
            print("Invalid analysis type.")
    elif cond == 'yes':
        # Getting the condition from user and applying it
        condition = input('Please enter the condition (e.g., >50):')
        try:
            for item in selected_data:
                if condition == True:
                    # Perform the selected analysis
                    if reply == 'find the sum of data' or reply == 'find the sum':
                        result = np.sum(selected_data)

                    elif reply in ['find the min of data', 'find the min']:
                        result = np.min(selected_data)

                    elif reply in ['find the max of data', 'find the max']:
                        result = np.max(selected_data)

                    elif reply in ['find the standard deviation of data', 'find the std']:
                        result = np.std(selected_data)

                    elif reply in ['find the mean of data', 'find the mean']:
                        result = np.mean(selected_data)

                    elif reply in ['find the median of data', 'find the median']:
                        result = np.median(selected_data)

                    elif reply in ['find the variance value of data', 'find the variance']:
                        result = np.var(selected_data)

                    elif reply in ['find percentile value']:
                        num_of_percentile = int(input('Enter the number of percentile:'))
                        result = np.percentile(selected_data,num_of_percentile)
                    
                    elif reply in ['find the cumulative sum']:
                        result = np.cumsum(selected_data)

                    elif reply in ['find the unique value']:
                        result = np.unique(selected_data)

                    else:
                        print("Invalid analysis type.")

    # Print or store the result
    print("Result:", result);
else:
    print("Error: More than one column selected.")

print(selected_data.head())
