condition = 'stopped'
while True:
   command = input('> ').strip().lower()
   if command == 'help':
      print('''
      Start - Start the car 
      Stop - Stop the car
      Cond - Gives condition of the car
      Quit - Quit the game
      ''')
   elif command == 'start' and condition == 'stopped':
      print('Your car has started.......')
      condition = 'running'
   elif command == 'start' and condition == 'running':
      print('Your car is already running!!!')
   elif command == 'stop' and condition == 'running':
      print('Your car has stopped.......')
      condition = 'stopped'
   elif command == 'stop' and condition == 'stopped':
      print('Your car has already stopped!!!')
   elif command == 'cond':
      print(condition)
   elif command == 'quit':
      break
   else:
      print('Enter the correct command!!')
  
   

