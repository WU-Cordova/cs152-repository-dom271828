class Cell:
    def __init__(self, alive: bool=False):
        self.alive = alive
    
    @property
    def is_alive(self) -> bool: 
        """ Getter for alive value """
        return self.alive
    
    @is_alive.setter
    def is_alive(self, alive = bool):
        """ Determines whether cell is alive based on a bool, 
         so it can retroactively be changed"""
        self.alive = alive

    def __eq__(self, value):
        """ Compares two alive variables, if both are the same
          then cells are considered to be equal. """
        if isinstance(value, Cell):
            return self.alive == value.alive
        return False
    
    def __str__(self): return "🦠" if self.alive else "  "