"""
Clone of 2048 game.
"""

import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    res = [0] * len(line)
    res_idx = 0
    last_tile = 0
    last_merged = False
    for tile in line:
        if tile != 0:
            if tile == last_tile and last_merged == False:  
                res[res_idx - 1] = last_tile + tile
                last_merged = True
            else:
                res[res_idx] = tile
                res_idx += 1 
                last_merged = False
            last_tile = tile
    return res
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.my_grid = [([0] * self.grid_width) for i in range(self.grid_height)]
        self.initial_tiles = {UP: [(0, i) for i in range(grid_width)], 
                              DOWN: [(grid_height - 1, i) for i in range(grid_width)], 
                              LEFT: [(i, 0) for i in range(grid_height)], 
                              RIGHT: [(i, grid_width - 1) for i in range(grid_height)]} 

    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.my_grid = [([0] * self.grid_width) for i in range(self.grid_height)]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.my_grid)


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        changed = False
        for side_tile in self.initial_tiles[direction]:
            if direction == UP or direction == DOWN:
                over_range = self.grid_height
            elif direction == LEFT or direction == RIGHT:
                over_range = self.grid_width
            else:
                print "Error, incorrect direction!"
            operate_tiles = []
            for i in range(over_range):
                operate_tiles.append(self.get_tile(side_tile[0] + OFFSETS[direction][0] * i, side_tile[1] + OFFSETS[direction][1] * i))
            new_tiles = merge(operate_tiles)
            if new_tiles != operate_tiles:
                changed = True
            for i in range(over_range):
                self.my_grid[side_tile[0] + OFFSETS[direction][0] * i][side_tile[1] + OFFSETS[direction][1] * i] = new_tiles[i]
        if changed ==True:
            self.new_tile()
                    
            
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_candidate = []
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if self.my_grid[i][j] == 0:
                    empty_candidate.append([i, j])
        grid_idx = random.choice(empty_candidate)
        row_idx = grid_idx[0]
        col_idx = grid_idx[1]
        if random.random() < 0.9:
            self.set_tile(row_idx, col_idx, 2)
        else:
            self.set_tile(row_idx, col_idx, 4)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """    
        self.my_grid[row][col] = value


    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.my_grid[row][col]
 

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
