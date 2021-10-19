n = 9
guess_counter = 0
while guess_counter < 3:
   a = int(input('Guess: '))
   if a == n:
      print('You guessed Correctly!')
      break
   else:
      guess_counter = guess_counter + 1
else:
      print('Your 3 chances are over!')