from random import random
from time import sleep

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

def render(*grid):
   new_grid = []
   for row in grid:
      new_grid.append(['##' if i==1 else '  'for i in row])
   for row in new_grid:
      for column in row:
         print(column, end="")
      print()

def next_state(grid):
   new_grid = []
   return new_grid
def run_forever(*initial_grid):
   grid = initial_grid
   while True:
      render(*grid)
      grid = next_state(grid)
      sleep(0.3)
      
      
board = random_state(10,10)
run_forever(*board)
