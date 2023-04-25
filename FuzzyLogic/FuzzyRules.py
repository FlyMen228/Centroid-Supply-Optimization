from skfuzzy import control as ctrl

from .FuzzyVariables import FuzzyVariables


class FuzzyRules:
    
    def __init__(self):
        
        self.fuzzy_variables = FuzzyVariables()
        
        self.rule1 = ctrl.Rule(
            self.fuzzy_variables.stock_status['minimum'] & 
            self.fuzzy_variables.time_in_stock['week1'] & 
            self.fuzzy_variables.sale['bad'] & 
            self.fuzzy_variables.order['little'], 
            self.fuzzy_variables.production['minimum'])
        
        self.rule18 = ctrl.Rule(
            self.fuzzy_variables.stock_status['minimum'] & 
            self.fuzzy_variables.time_in_stock['week2'] & 
            self.fuzzy_variables.sale['good'] & 
            self.fuzzy_variables.order['reasonable'], 
            self.fuzzy_variables.production['maximum'])
        
        self.rule35 = ctrl.Rule(
            self.fuzzy_variables.stock_status['minimum'] & 
            self.fuzzy_variables.time_in_stock['week3'] & 
            self.fuzzy_variables.sale['great'] & 
            self.fuzzy_variables.order['much'], 
            self.fuzzy_variables.production['maximum'])
        
        self.rule65 = ctrl.Rule(
            self.fuzzy_variables.stock_status['median'] & 
            self.fuzzy_variables.time_in_stock['week1'] & 
            self.fuzzy_variables.sale['good'] & 
            self.fuzzy_variables.order['much'], 
            self.fuzzy_variables.production['minimum'])
        
        self.rule38 = ctrl.Rule(
            self.fuzzy_variables.stock_status['median'] & 
            self.fuzzy_variables.time_in_stock['week2'] & 
            self.fuzzy_variables.sale['bad'] & 
            self.fuzzy_variables.order['little'], 
            self.fuzzy_variables.production['not'])
        
        self.rule59 = ctrl.Rule(
            self.fuzzy_variables.stock_status['median'] & 
            self.fuzzy_variables.time_in_stock['week3'] & 
            self.fuzzy_variables.sale['great'] & 
            self.fuzzy_variables.order['reasonable'], 
            self.fuzzy_variables.production['minimum'])
        
        self.rule97 = ctrl.Rule(
            self.fuzzy_variables.stock_status['maximum'] & 
            self.fuzzy_variables.time_in_stock['week1'] & 
            self.fuzzy_variables.sale['bad'] & 
            self.fuzzy_variables.order['much'], 
            self.fuzzy_variables.production['not'])
        
        self.rule82 = ctrl.Rule(
            self.fuzzy_variables.stock_status['maximum'] & 
            self.fuzzy_variables.time_in_stock['week2'] & 
            self.fuzzy_variables.sale['great'] & 
            self.fuzzy_variables.order['little'], 
            self.fuzzy_variables.production['minimum'])

        self.rule92 = ctrl.Rule(
            self.fuzzy_variables.stock_status['maximum'] & 
            self.fuzzy_variables.time_in_stock['week4'] & 
            self.fuzzy_variables.sale['good'] & 
            self.fuzzy_variables.order['reasonable'], 
            self.fuzzy_variables.production['minimum'])
    
    
    def get_all_rules(self):
        
        return [self.rule1, self.rule18, self.rule35, self.rule65, self.rule38, self.rule59, self.rule97, self.rule82, self.rule92]