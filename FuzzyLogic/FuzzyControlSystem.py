import skfuzzy as fuzzy
from skfuzzy import control as ctrl

from .FuzzyRules import FuzzyRules


class FuzzyControlSystem:
    
    def __init__(self):
        
        self.fuzzy_rules = FuzzyRules()
        
        self.control_system = ctrl.ControlSystem(self.fuzzy_rules.get_all_rules())
        
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)
        
    def fuzzy_control_system(self, data_row):
        
        self.simulation.input['Stock Status'] = data_row['Stock Status']
        self.simulation.input['Sales'] = data_row['Sales']
        self.simulation.input['Orders'] = data_row['Orders']
        self.simulation.input['Time In Stock'] = data_row['Time In Stock']
        
        try:
            self.simulation.compute()
        except Exception as ex:
            return None
        
        return self.simulation.output['Production']