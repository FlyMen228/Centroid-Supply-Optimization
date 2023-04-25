import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tqdm._tqdm_notebook import tqdm_notebook
tqdm_notebook.pandas()

import seaborn as sns
sns.set()

from FuzzyLogic.FuzzyControlSystem import FuzzyControlSystem


def read_data_from_file():

    data = pd.read_csv('input.txt', sep = ',', names = ['ID', 'Name', 'Quantity', 'Stock Status', 'Orders', 'Sales', 'Time In Stock', 'Date'])

    data['ID'] = data['ID'].astype(int)
    data['Name'] = data['Name'].astype(str)
    data['Quantity'] = data['Quantity'].astype(int)
    data['Stock Status'] = data['Stock Status'].astype(int)
    data['Orders'] = data['Orders'].astype(int)
    data['Sales'] = data['Sales'].astype(int)
    data['Time In Stock'] = data['Time In Stock'].astype(int)
    data['Date'] = pd.to_datetime(data['Date'])

    return data


def main():

    data = read_data_from_file()

    fuzzy_control_system = FuzzyControlSystem()

    for index, row in data.iterrows():
        
        output = fuzzy_control_system.fuzzy_control_system(row)
        
        print(output)
        
        with open('output.txt', mode = 'a') as output_file:
            
            output_file.write(' '.join(str(x) for x in row) + ' ' + str(output))


if __name__ == '__main__':

    main()