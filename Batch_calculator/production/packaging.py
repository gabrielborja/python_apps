class Packaging():
    KINDS = ("single", "2pk", "løsvekt")
    
    def __init__(self, kind):
        if kind not in self.KINDS:
            raise ValueError(f"Invalid packaging kind. Kind must be one of the following: {self.KINDS}")
        self.kind = kind
    
    def __str__(self):
        return f"{self.kind}"
    def __repr__(self):
        return f"Packaging('{self.kind}')"