from random import randint

players = {}
# to preserve the existing leaderboard
with open("leaderboard.txt", 'r') as f:
    for line in f:
        players[line.split()[0]] = int(line.split()[1])


def game():

    print('''
                            Welcome to Number Guessing Game
            
    You have to correctly guess the number between 1 to 100 in as less turns as possible

    Type "help" to know the commands''')
    while True:
        cmd = input('enter command: ').strip().lower()
        if cmd == 'play':
            play()
        elif cmd == 'quit':
            break
        elif cmd == 'help':
            help()
        elif cmd == 'lead':
            leaderboard()


def help():
    """(None) -> str \n
    Displays a list of commands
    """
    print("""
          play      Start the game
          quit      Exit the game
          lead      Displays leaderboard
          """)


def play():
    """(None) -> None \n
    starts the game
    """

    num = randint(1, 100)
    print(num)
    count = 0
    name = input("Enter your username: ").strip().lower()
    while True:
        try:
            guess = int(input('Enter your guess: '))
        except:
            print("Please enter a valid integer")
            continue
        count += 1
        if guess > num:
            print("You guessed too high!")
        elif guess < num:
            print("You guessed too low")
        elif guess == num:
            if count == 1:
                print("Lady luck smiles upon you! \nYou guessed it just 1 turn!")
                players[name] = players.get(name, 0) + count
                break
            print("You guessed correctly! \nIt took you",
                  count, "turns to guess correctly")
            players[name] = players.get(name, 0)
            players[name] = count

            break
    with open('leaderboard.txt', 'w') as f:
        for name, count in sorted(players.items(), key=lambda x: x[1]):
            f.write("{} {}\n".format(name, count))


def leaderboard():
    """(None) -> None
    Prints the leaderboard
    """
    print("{name:<15}{score:<5}".format(name='NAME', score='SCORE'))
    with open("leaderboard.txt", 'r') as f:
        for line in f:
            print("{name:<15}{score:<5}".format(
                name=line.split()[0], score=line.split()[1]))


if __name__ == '__main__':
    game()
