import re
class regex_cls:
    def __init__(self,amount_formula):
        self.amount_formula = amount_formula
        self.no_formula = '^ETR.AMOUNT.(\w*)'

    def evaluate_formula(self):
        result = re.search(self.no_formula,self.amount_formula)
        
        if len(result.groups()) > 0:
            print("Found Aount Field {0}".format(result.group(1)))
        else:
            print("Amount field not found!!!")