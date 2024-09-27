from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self):
        self.name = name 
    def get_name(self):
        return self.name
    def set_name(self):
        pass
    
class String_Instrument(Instrument):
    def __init__(self):
        self.num_of_strings = num_of_strings
    def getter(self):
        return self.num_of_strings
    def setter(self):
        pass

v = String_Instrument("Violin", 4)
