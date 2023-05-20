import sqlite3


connection = sqlite3.connect('Warhouse.sqlite')

cursor = connection.cursor()


############ Блок сброса таблиц перед инициализацией ############

cursor.execute('Drop Table If Exists Products')
cursor.execute('Drop Table If Exists Stuff')
cursor.execute('Drop Table If Exists Products_log')
cursor.execute('Drop Table If Exists Stuff_log')
cursor.execute('Drop Table If Exists Orders')
cursor.execute('Drop Table If Exists Ordered_Products')
cursor.execute('Drop Table If Exists Deliveries')
cursor.execute('Drop Table IF Exists Optimization_log')

#############################################################


############ Блок создания таблиц ############

cursor.execute('''Create Table if Not Exists Products (
    p_id Integer,
    p_name varchar(100) Not Null,
    p_quantity int Default 0,
    p_price numeric Default 0,
    p_stock_status int Default 0,
    p_orders int Default 0,
    p_sales numeric Default 0,
    p_time_in_stock int Default 1,
    p_supply_date timestamp,
    Constraint PK_Products Primary Key(p_id),
    Constraint UQ_Products_name Unique(p_name),
    Constraint CK_Products_quantity Check(p_quantity >= 0),
    Constraint CK_Products_stock_status Check(p_stock_status >= 0 and p_stock_status <= 100),
    Constraint CK_Products_orders Check(p_orders >= 0),
    Constraint CK_Products_sales Check(p_sales >= 0),
    Constraint CK_Products_time_in_stock Check(p_time_in_stock >= 1 and p_time_in_stock <= 28),
    Constraint CK_Products_price Check(p_price >= 0))''')


cursor.execute('''Create Table If Not Exists Optimization_log (
    ol_id Integer Primary Key,
    ol_p_id int,
    ol_stock_status int,
    ol_orders int,
    ol_sales numeric,
    ol_time_in_stock int,
    ol_production_varchar varchar(20),
    ol_production_numeric numeric,
    ol_date timestamp Default Current_Timestamp,
    Foreign Key (ol_p_id) References Products(p_id))''')

#############################################################


connection.close()