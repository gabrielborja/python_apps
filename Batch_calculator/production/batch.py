from datetime import datetime
from datetime import timedelta

class Batch():
    _LØSVEKT = ("Melk", "Smi")
    _TWO_PACK = ("Dai", "Milk", "Smi")
    _SINGLE = ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw")

    def __init__(self, name, kind, boxes):
        if kind == "2pk" and name not in self._TWO_PACK:
            raise ValueError(f"Invalid name for two-pack. Name must be one of the following: {self._TWO_PACK}")
        elif kind == "løsvekt" and name not in self._LØSVEKT:
            raise ValueError(f"Invalid name for løsvekt. Name must be one of the following: {self._LØSVEKT}")
        elif kind == "single" and name not in self._SINGLE:
            raise ValueError(f"Invalid name for single. Name must be one of the following: {self._SINGLE}")
        self.name = name
        self.kind = kind
        self.date = datetime.now()
        self.boxes = boxes
    
    def __str__(self):
        return f"{self.boxes} boxes of '{self.name}' '{self.kind}'"
    
    def __repr__(self):
        return f"Batch(name = '{self.name}', kind = '{self.kind}', boxes = {self.boxes})"
    
    def boxes_per_hour(self):
        return 60 if self.kind == "løsvekt" else 180 if self.kind == "2pk" else 444
    
    def calculate_time_to_produce(self):
        return divmod(self.boxes, self.boxes_per_hour())

    def display_time_to_produce(self):
        hours, minutes = self.calculate_time_to_produce()
        return f"{hours} hours {minutes} min"
    
    def display_time_to_finish(self):
        hours, minutes = self.calculate_time_to_produce()
        seconds = hours * 3600 + minutes * 60
        now = self.date + timedelta(seconds = seconds)
        return f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}"
    