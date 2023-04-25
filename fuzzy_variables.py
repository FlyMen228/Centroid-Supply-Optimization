import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl


stock_status = ctrl.Antecedent(np.arange(0, 100, 1), 'Stock Status')
sale = ctrl.Antecedent(np.arange(0, 25, 0.001), 'Sale') #*10^3
order = ctrl.Antecedent(np.arange(0, 100, 5), 'Order')


stock_status['minimum'] = fuzzy.trapmf(stock_status.universe, [0, 0, 20, 40])
stock_status['median'] = fuzzy.trimf(stock_status.universe, [20, 50, 80])
stock_status['maximum'] = fuzzy.trapmf(stock_status.universe, [60, 80, 100, 100])

sale['bad'] = fuzzy.trapmf(sale.universe, [0, 0, 2, 3])
sale['good'] = fuzzy.trapmf(sale.universe, [2, 3.001, 7, 7.5])
sale['great'] = fuzzy.trapmf(sale.universe, [7, 7.501, 25, 25])

order['little'] = fuzzy.trimf(order.universe, [0, 0, 20, 25])
order['reasonable'] = fuzzy.trimf(order.universe, [20, 25, 50, 55])
order['much'] = fuzzy.trimf(order.universe, [50, 55, 100, 100])