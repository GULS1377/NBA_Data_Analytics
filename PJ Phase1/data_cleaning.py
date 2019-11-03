import pandas as pd
import numpy as np


# check error
def check_error(source, error_list, save_to_excel=False):
    error_dataframe = pd.DataFrame(columns=['error_row_index', 'error_type', 'error_row_value'])
    error_index =[]
    for error in error_list:
        for index, value in source.iterrows():
            for item in value:
            	# if there is any error, add it to the dataframe
                if item == error:
                    error_index.append(index)
                    error_dataframe = error_dataframe.append({
                        'error_row_index': index,
                        'error_type': error,
                        'error_row_value': value.values
                    }, ignore_index=True)
    # save the result
    if save_to_excel == True:
        error_dataframe.to_excel('Error_table.xlsx', index=False)
    return error_index

# print correct percentage for each column
def print_error_percentage(source, error_list):
    total_number = len(source)
    for index in range(len(source.columns)):
        error_number = 0
        for error in error_list:
            number = np.count_nonzero(source[index] == error)
            error_number += number
        print("Column ", index, "correct percentage:", (1 - error_number / total_number) * 100, "%")

# define clean process
def clean_process(source, error_index, save_to_excel=False):
    temp = source.drop(index=error_index)
    if save_to_excel == True:
        temp.to_excel('Clean_table.xlsx', index=False)
    return temp


# read csv file
source = pd.read_csv('result.csv', header=None)
# define error list
error_list = ["None", "< $Minimum"]
print("Current error list:", error_list)
# check error in the original data set
error_index = check_error(source, error_list, save_to_excel=True)
print('All errors are stored in the Error_table.xlsx Excel file')
print('Error row index:', error_index)
# print correct percentage
print_error_percentage(source, error_list)
# clean the dataset
cleaned_dataset = clean_process(source, error_index, save_to_excel=True)
print("After clean work, the new clean dataset is store in the Clean_table.xlsx file.")
# After the dataset is clean, re-run the check program and see the error index
check_error(cleaned_dataset, error_list, save_to_excel=False)
result_index = check_error(cleaned_dataset, error_list, save_to_excel=False)
print("After clean, the error index:", result_index)