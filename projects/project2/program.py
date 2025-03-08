from projects.project2.kbhit import *
from datastructures.array2d import Array2D
from projects.project2.grid import Grid
from projects.project2.cell import Cell
from projects.project2.gamecontroller import GameController

def main():
    grid = Grid(5, 5)
    game_controller = GameController(grid)
    game_controller.run()

if __name__ == '__main__':
    main()