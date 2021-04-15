import pandas as pd

class Product:
    _PRODUCTS = {'Prod_1' : 240, 'Prod_2': 45, 'Prod_3' : 30}

    def __init__(self, prod1, prod2):
        self.prod1 = prod1
        self.prod2 = prod2
    
    def locate_keys(self):
        return list(_PRODUCTS.keys())
    
    def locate_products(self):
        return _PRODUCTS.xs(self.prod1, axis=0, level=None)[self.prod2].to_dict()


product = Product('Prod_1', 'Prod_2')
product.locate_keys()
    
    
    