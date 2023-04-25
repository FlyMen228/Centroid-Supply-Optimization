import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl


class FuzzyVariables:

    def __init__(self):
        
        self.stock_status = ctrl.Antecedent(np.arange(0, 100, 1), 'Stock Status')
        self.sale = ctrl.Antecedent(np.arange(0, 25, 0.001), 'Sales') #10^3
        self.order = ctrl.Antecedent(np.arange(0, 100, 5), 'Orders')
        self.time_in_stock = ctrl.Antecedent(np.arange(1, 28, 1), 'Time In Stock')

        self.production = ctrl.Consequent(np.arange(0, 50, 0.001), 'Production') #10^3

        self.stock_status['minimum'] = fuzzy.trapmf(self.stock_status.universe, [0, 0, 20, 40])
        self.stock_status['median'] = fuzzy.trimf(self.stock_status.universe, [20, 50, 80])
        self.stock_status['maximum'] = fuzzy.trapmf(self.stock_status.universe, [60, 80, 100, 100])

        self.sale['bad'] = fuzzy.trapmf(self.sale.universe, [0, 0, 2, 3])
        self.sale['good'] = fuzzy.trapmf(self.sale.universe, [2, 3.001, 7, 7.5])
        self.sale['great'] = fuzzy.trapmf(self.sale.universe, [7, 7.501, 25, 25])

        self.order['little'] = fuzzy.trapmf(self.order.universe, [0, 0, 20, 25])
        self.order['reasonable'] = fuzzy.trapmf(self.order.universe, [20, 25, 50, 55])
        self.order['much'] = fuzzy.trapmf(self.order.universe, [50, 55, 100, 100])

        self.time_in_stock['week1'] = fuzzy.trapmf(self.time_in_stock.universe, [0, 0, 5, 7])
        self.time_in_stock['week2'] = fuzzy.trapmf(self.time_in_stock.universe, [5, 8, 10, 14])
        self.time_in_stock['week3'] = fuzzy.trapmf(self.time_in_stock.universe, [12, 15, 19, 21])
        self.time_in_stock['week4'] = fuzzy.trapmf(self.time_in_stock.universe, [18, 22, 28, 28])

        self.production['not'] = fuzzy.trapmf(self.production.universe, [0, 0, 0, 0])
        self.production['minimum'] = fuzzy.trapmf(self.production.universe, [0.001, 5, 12, 12.5])
        self.production['maximum'] = fuzzy.trapmf(self.production.universe, [12, 12.5, 50, 50])
