import functions

print('''
                        Welcome to Number Guessing Game
        
You have to correctly guess the number between 1 to 100 in as less turns as possible

Type "help" to know the commands''')
while True:
    cmd = input('enter command: ').strip().lower()
    if cmd == 'play':
        functions.play()
    elif cmd == 'quit':
        break
    elif cmd == 'help':
        functions.help()
    elif cmd == 'lead':
        functions.leaderboard()
