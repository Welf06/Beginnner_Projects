from tokenize import Triple


print("4 DOT GAME")
def emty_grid():
   return [['0' for j in range(6)] for i in range(4)]

def display_grid(grid):
   for i in grid[::-1]:
      print('|'.join(i))
      
def even(column, grid):
   for i in grid:
      if i[column-1] == '0':
         i[column-1] = '1'
         break
   for i in grid:
      if '0' in i:
         break
   else:
      print("Game over")
      return exit
def odd(column, grid):
   for i in grid:
      if i[column-1] == '0':
         i[column-1] = '2'
         break
   for i in grid:
      if '0' in i:
         break
   else:
      print("Game over")
      
def game():
   turn = 0
   grid = emty_grid()
   status = True
   display_grid(grid)
   while status:
      try:
         grid_spot = int(input(f"Player {turn%2 +1} please enter the row: "))
         if turn %2 ==0:
            even(grid_spot, grid)
            
         else:
            odd(grid_spot, grid)
      except:
         continue
      turn += 1
      display_grid(grid)
   
game()