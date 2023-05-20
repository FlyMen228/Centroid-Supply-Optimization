import skfuzzy as sk

from skfuzzy import control as ctrl

from .FuzzyRules import FuzzyRules
from .FuzzyVariables import FuzzyVariables


class FuzzyControlSystem:

    def __init__(self):

        self.fuzzy_rules = FuzzyRules()
        
        self.control_system = ctrl.ControlSystem(self.fuzzy_rules.get_all_rules())
        
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)
        
        self.fuzzy_variables = FuzzyVariables()


    def compute(self, data_row):
        
        self.simulation.input['Stock Status'] = data_row['p_stock_status']
        self.simulation.input['Sales'] = data_row['p_sales']
        self.simulation.input['Orders'] = data_row['p_orders']
        self.simulation.input['Time In Stock'] = data_row['p_time_in_stock']
        
        try:
            self.simulation.compute()
        except Exception as ex:
            return (str('No Rule'), float(0))

        decimal_part = str(round(self.simulation.output['Production'], 2)).split('.')[1]
        compute_result = float('0.' + decimal_part)

        if 0 <= compute_result <= 0.25:
            lingv_ver = 'not'
        elif 0.26 <= compute_result <= 0.74:
            lingv_ver = 'minimum'
        else:
            lingv_ver = 'maximum'

        return(lingv_ver, compute_result)