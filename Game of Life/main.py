from random import random
from time import sleep

# function to generate a sandom grid
def random_state(row, column):
   grid = []
   for i in range(row):
      row = []
      for j in range(column):
         if random() > 0.75:
            row.append(1)
         else:
            row.append(0)
      grid.append(row)
   return grid

# function to generate a new grid based on a grid following these rules:
# # Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
# Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
# Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
def next_state(*grid):
   row = len(grid)
   column = len(grid[0])
   new_grid = [[0 for x in range(column)] for y in range(row)]
   for i in range(row):
      for j in range(column):
         current_cell = grid[i][j]
         # for corner cells
         if (i == 0 and j == 0) or (i == row-1 and j == column -1) or (i == 0 and j == column-1) or (i == row-1 and j == 0):
            continue
         # edge cases
         elif i==0 or j == 0 or i == row-1 or j == column -1:
            continue
         # for non edge rows 
         else:
            # row above the current cell
            live_value = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
            # row of the current cell
            live_value += grid[i][j-1] + grid[i][j+1]
            # row below the current cell
            live_value += grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
            if current_cell == 0 and live_value == 3:
               new_grid[i][j] = 1
            elif current_cell == 1:
               if live_value < 2:
                  pass
               elif live_value < 4:
                  new_grid[i][j] = 1
               elif live_value > 3 :
                  pass
      
   return new_grid

def render(*grid):
   new_grid = []
   for row in grid:
      new_grid.append(['##' if i==1 else '  'for i in row])
   for row in new_grid:
      for column in row:
         print(column, end="")
      print()

def run_forever(*initial_grid):
   grid = initial_grid
   while True:
      render(*grid)
      grid = next_state(*grid)
      sleep(0.3)
if __name__== '__main__':
   board = random_state(100,100)
   run_forever(*board)
   # print(next_state(*board))
