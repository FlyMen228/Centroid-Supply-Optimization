import sqlite3
import pandas as pd

from prettytable import from_db_cursor


def print_products():

    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()
    
    cursor.execute('Select * From Products')

    products_table = from_db_cursor(cursor)
    
    print(products_table)

    connection.close()
   
    
def print_optimization_log():
    
    connection = sqlite3.connect('Warhouse.sqlite')

    cursor = connection.cursor()
    
    cursor.execute('''Select P.p_name, OL.ol_stock_status, OL.ol_orders, OL.ol_sales, OL.ol_time_in_stock, 
                             OL.ol_production_varchar, OL.ol_production_numeric, OL.ol_date 
        From Optimization_log OL Join Products P On OL.ol_p_id = P.p_id
        Order By OL.ol_p_id''')

    ol_table = from_db_cursor(cursor)
    
    print(ol_table)

    connection.close()
    

def fetchall_products():

    connection = sqlite3.connect('Warhouse.sqlite')
    
    query = '''Select * From Products'''

    data = pd.read_sql_query(query, connection)

    connection.close()
    
    return data


def fetchall_optimization_log():
    
    connection = sqlite3.connect('Warhouse.sqlite')
    
    query = '''Select P.p_name, OL.ol_stock_status, OL.ol_orders, OL.ol_sales, OL.ol_time_in_stock, OL.ol_production, OL.ol_date 
        From Optimization_log OL Join Products P On OL.ol_p_id = P.p_id
        Order By OL.ol_p_id'''
        
    data = pd.read_sql_query(query, connection)
    
    connection.close()
    
    return data


def insert_optimization(row):
    
    connection = sqlite3.connect('Warhouse.sqlite')
    
    cursor = connection.cursor()
    
    insert = [(row[0], row[4], row[5], row[6], row[7], row[9], row[10])]

    cursor.executemany('''Insert Into Optimization_log (ol_p_id, ol_stock_status, ol_orders, ol_sales, ol_time_in_stock, ol_production_varchar, ol_production_numeric)
        values(?, ?, ?, ?, ?, ?, ?)''', insert)
    
    connection.commit()
    
    connection.close()