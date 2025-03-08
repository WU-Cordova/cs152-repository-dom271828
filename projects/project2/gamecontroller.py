from projects.project2.grid import Grid
from time import sleep
from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self, grid: Grid):
        self.grid = grid # Grid is entered upon initiation
        self.history = [] # Stores three previous grid values
        self.gen = 0 # Makes it so display command accurately prints generation #
        self.broken = False # Loop breaks if this is true
    
    def cycle(self) -> None:
        """ 
        Function that:
            - Iterates through history and breaks loop if game is stable.
            - Creates a grid new_grid based on the next generation of current self.grid
            - Displays this new grid. 
            - Appends new self.grid to list self.history. 
        """
        if len(self.history) == 3:
            dupes = []
            for grid in self.history:
                if grid in dupes:
                    print("Game ended due to nonstability")
                    self.broken = True
                    return
                dupes.append(grid)
            self.history.pop(0) # pops earliest iteration to make room for newest grid
        self.gen += 1 # Embellishes display command
        new_grid = self.grid.next_generation() # new grid created off of generation of old grid
        new_grid.display(self.gen) 
        self.grid = new_grid 
        self.history.append(self.grid) # appends to history

    def run(self):
        """
        Function that:
        - Gets mode based on user input.
        - Loops while capturing input with KBHit
        - Breaks when 'q' is pressed or self.broken == True
        """
        manual = False # Manual variable false 
        response = input("Do you prefer (m)anual or (a)utomatic mode? ").strip().lower() # unfortunately couldn't get it to work with kbhit.
        # I'm sure there's a more efficient solution to this, but this is all I have
        if response == 'm':
            print("Press s to print another generation. Press q to quit.")
            manual = True
        elif response == 'a':
            print("Press q to quit.")
        else:
            print("Invalid key.")
            return
        
        while True:
            state = KBHit() 

            while True: 
                if self.broken:
                    return
                
                if state.kbhit():

                    key = state.getch()

                    if key == 'q': # Works with both modes
                        print("You hit quit")
                        return
                    
                    if key == 's' and manual == True: # Won't activate in automatic mode
                        self.cycle()
                
                if manual == False: # Won't activate in manual mode
                    sleep(1)
                    self.cycle()
