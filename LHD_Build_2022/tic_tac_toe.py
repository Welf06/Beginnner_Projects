from tokenize import Triple


print("Tic Tac Toe")
def emty_grid():
   return [['0' for j in range(3)] for i in range(3)]

def display_grid(grid):
   for i in grid[::-1]:
      print('|'.join(i))
      
def even(column, grid):
   for i in grid:
      if i[column-1] == '0':
         i[column-1] = '1'
         break

def odd(column, grid):
   for i in grid:
      if i[column-1] == '0':
         i[column-1] = '2'
         break
      
def check_board(grid, turn):
   if ['1','1','1'] in grid or ['2','2','2'] in grid:
      print(f"Player {turn%2+1} won !")
      return False
   elif turn == 8:
      print("Draw")
      return False
   else:
      return True
   
   
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
         status = check_board(grid, turn)
      except:
         turn -= 1
         continue
      turn += 1
      display_grid(grid)
   
game()