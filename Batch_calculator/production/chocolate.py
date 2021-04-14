class Chocolate():
    BRANDS = ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw")
    
    def __init__(self, name):
        if name not in self.BRANDS:
            raise ValueError(f"Invalid chocolate name. Name must be one of the following: {self.BRANDS}")
        self.name = name
        
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"Chocolate('{self.name}')"