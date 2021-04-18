import pandas as pd

class Product():
    """Convert from one manufacturing product to a second product from available list.
    Return the product id code, group category and time in minutes needed to change
    from one product to another (changeover time).
    
    Parameters
    ----------
    prod1 = str of first product name from data/matrix.csv
    prod2 = str of second product name from data/matrix.csv"""

    _DF = pd.read_csv('data/matrix.csv', index_col=[0], header=[0, 1, 2])
    
    #Initialize object state
    def __init__(self, prod1='Prod1', prod2='Prod2'):
        self.prod1 = prod1
        self.prod2 = prod2

    #Printable representation string
    def __repr__(self):
        return f"Product(prod1='{self.prod1}', prod2='{self.prod2}')" 
    
    #Show first 5 rows of matrix of available products
    def show_matrix(self):
        return self._DF.head()

    #List of available products
    def list_all_products(self):
        return list(self._DF.index)
    
    #Locate a product code, group and changeover time
    def locate_product(self):
        return self._DF.xs(self.prod1, axis=0, level=None)[self.prod2].to_dict()


product1 = Product('Prod_1', 'Prod_3')
product2 = Product('Prod_4', 'Prod_20')