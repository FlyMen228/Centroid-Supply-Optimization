import sqlite3
from datetime import datetime


connection = sqlite3.connect('Warhouse.sqlite')

cursor = connection.cursor()


current_time = "2023-05-06 20:00:00" # Дата и время для быстроты ввода


############ Блок очистки таблиц перед вставками ############

cursor.execute('Delete From Products')
connection.commit()

#############################################################


############ Блок вставок ############

    #name, quantity, price, ss, orders, sale, tis, date
productsArr = [
    ("Хозяйственное мыло", 15000, 120.40, 10, 1, 1, 4, current_time), #r1
    ("Дезодорант 'Captain' Old Spice", 200000, 320.49, 25, 50, 2500, 20, current_time), #r59
    ("Гель для бритья Akino", 1200, 100.99, 35, 50, 3000, 14, current_time), #59
    ("Крем-гель для умывания 'Красота и Здоровье' Nivea", 0, 200, 10, 1, 1, 4, current_time), #r1
    ("Гель для бритья 'Свежесть и защита' Gillette", 30, 4000.99, 97, 54, 7, 28, current_time), #r92
    ("Гель для бритья 'Гладкость и уход' L'Oreal Men Expert", 1337, 200, 17, 28, 6.32, 11, current_time), #r18
    ("Крем для рук 'Бережный уход' Dove", 3012, 123.03, 84, 19, 19.032, 12, current_time), #r82
    ("Лосьон для тела 'Увлажнение и питание' Nivea", 228, 322.37, 72, 19, 0, 13, current_time) #r38
]

cursor.executemany('''Insert Into Products (p_name, p_quantity, p_price, p_stock_status, p_orders, p_sales, p_time_in_stock, p_supply_date) Values (?, ?, ?, ?, ?, ?, ?, ?)''', productsArr)

connection.commit()

#############################################################


connection.close()