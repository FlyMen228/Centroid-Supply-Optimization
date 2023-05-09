import pandas as pd

from FuzzyLogic.FuzzyControlSystem import FuzzyControlSystem
from DataBase import queries


def main():

    fuzzy_control_system = FuzzyControlSystem()
    
    data = queries.fetchall_products()
    
    for index, row in data.iterrows():
        
        result = fuzzy_control_system.compute(row)
        
        queries.insert_optimization(row, result)


if __name__ == '__main__':

    main()