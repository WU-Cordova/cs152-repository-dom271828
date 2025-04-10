from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import copy
import random

class Grid:
    def __init__(self, rows: int, cols: int):
        self.grid: Array2D[Cell] = Array2D.empty(rows, cols, data_type=Cell) # List of lists

        self.rows = rows
        self.cols = cols

        for row in range(rows):
            for col in range(cols):
                self.grid[row][col].is_alive = random.choice([True, False])

    def display(self, g: int) -> None:
        """ Displays complete cell diagram. """
        print(f"Generation {g}:") # g is usually the value of self.gen in gamecontroller file
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end="")
            print()      

    def get_neighbors(self, row, col): # Brute force version
        """ Gets all eight neighbor values, or less if invalid.
        Returns number of neighbors """
        neighbors = 0

        if row + 1 < self.rows and str(self.grid[row + 1][col]) == "🦠": # checks above for neighbor
            neighbors += 1
        
        if col + 1 < self.cols: # nested statement b/c returns index error if I use string command
            if str(self.grid[row][col + 1]) == "🦠": # checks right for neighbor
                neighbors += 1
        
        if col + 1 < self.cols and row + 1 < self.rows:
            if str(self.grid[row + 1][col + 1]) == "🦠": # checks diagonally up/right for neighbor
                neighbors += 1
        
        if row > 0 and str(self.grid[row - 1][col]) == "🦠": # checks above for neighbor
            neighbors += 1

        if col > 0 and str(self.grid[row][col - 1]) == "🦠": # checks left for neighbor
            neighbors += 1

        if row > 0 and col > 0 and str(self.grid[row - 1][col - 1]) == "🦠": # checks diagonally up/right for neighbor
            neighbors += 1

        if row + 1 < self.rows and col > 0:
            if str(self.grid[row + 1][col - 1]) == "🦠": # checks diagonally 
                neighbors += 1
        
        if row > 0 and col + 1 < self.cols:
            if str(self.grid[row - 1][col + 1]) == "🦠":
                neighbors += 1

        return neighbors

    def next_generation(self):
        """Returns grid object with cells changed based on num_neighbors,
        Iterates throguh self.grid in most cases."""
        next_grid = (Grid(self.rows, self.cols)) 
        for row in range(self.rows):
            for col in range(self.cols):
                num_neighbors = self.get_neighbors(row, col)
                if num_neighbors < 1 or num_neighbors >= 4: # Cell dies of over/underpopulation
                    next_grid.grid[row][col] = Cell(alive=False)
                elif num_neighbors == 2: # Cell stays the same
                    next_grid.grid[row][col] = self.grid[row][col]
                elif num_neighbors == 3: # New cell
                    next_grid.grid[row][col] = Cell(alive=True)
        return next_grid
        
    def __eq__(self, value):
        """Returns True if grid contains the same values"""
        if isinstance(value, Grid) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid # True if grid is the same size w/same values, False if grid is only the same size
        return False 