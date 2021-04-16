import pandas as pd

class Product():
    _DF = pd.read_csv('data/matrix.csv', index_col=[0], header=[0, 1, 2])
    
    def __init__(self, prod1, prod2):
        self.prod1 = prod1
        self.prod2 = prod2
    
    def show_matrix(self):
        return self._DF.head()

    def locate_keys(self):
        return list(self._DF.index)
    
    def locate_product(self):
        return self._DF.xs(self.prod1, axis=0, level=None)[self.prod2].to_dict()


product1 = Product('Prod_1', 'Prod_3')
product2 = Product('Prod_4', 'Prod_20')