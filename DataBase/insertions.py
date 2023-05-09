import sqlite3
from datetime import datetime


connection = sqlite3.connect('Warhouse.sqlite')

cursor = connection.cursor()


current_time = "2023-05-06 20:00:00" # Дата и время для быстроты ввода


############ Блок очистки таблиц перед вставками ############

cursor.execute('Delete From Products')
connection.commit()

cursor.execute('Delete From Stuff')
connection.commit()

cursor.execute('Delete From Orders')
connection.commit()

cursor.execute('Delete From Ordered_Products')
connection.commit()

cursor.execute('Delete From Deliveries')
connection.commit()

cursor.execute('Delete From Products_log')
connection.commit()

cursor.execute('Delete From Stuff_log')
connection.commit()

#############################################################


############ Блок вставок ############

productsArr = [
    ("Дезодорант 'Captain' Old Spice", 200000, 320.49, 20, 20, 2500, 6, current_time),
    ("Гель для бритья Akino", 1200, 100.99, 35, 50, 3000, 14, current_time),
    ("Гель для умывания", 0, 200, 0, 0, 0, None, None)
]

cursor.executemany('''Insert Into Products (p_name, p_quantity, p_price, p_stock_status, p_orders, p_sales, p_time_in_stock, p_supply_date) Values (?, ?, ?, ?, ?, ?, ?, ?)''', productsArr)

connection.commit()


stuffArr = [
    ("Абрамзон А.А.", "Creator", "111-111"),
    ("Шакиров Д.И.", "Admin", "777-777"),
    ("Ванслов Г.Д.", "Deliverer", "666-666")
]

cursor.executemany('''Insert Into Stuff (s_fullname, s_role, s_phone) Values (?, ?, ?)''', stuffArr)

connection.commit()


ordersArr = [
    ("No", None),
    ("Yes", "г. Челябинск, ул. Б. Кашириных 129"),
    ("Yes", "г. Челябинск, ул. Кузнецова 12")
] #Должно быть 3 столбца, но дата по-умолчанию - текущее время.

cursor.executemany('''Insert Into Orders (o_delivery, o_address) Values (?, ?)''', ordersArr)

connection.commit()


ordersArrWDate = [
    ("No", None, current_time)
] #Со столбцом даты.

cursor.executemany('''Insert Into Orders (o_delivery, o_address, o_date) Values (?, ?, ?)''', ordersArrWDate)

connection.commit()


opArr = [
    (1, 1, 5),
    (2, 1, 5),
    (1, 2, 400),
    (2, 3, 100),
    (3, 3, 100),
    (1, 3, 23),
    (2, 4, 1)
]

cursor.executemany('''Insert Into Ordered_Products (op_product_id, op_order_id, op_quantity) Values (?, ?, ?)''', opArr)

connection.commit()


deliveriesArr = [
    (2, 3),
    (3, 3)
]

cursor.executemany('''Insert Into Deliveries (d_order_id, d_deliverer_id) Values (?, ?)''', deliveriesArr)

connection.commit()

#############################################################


connection.close()