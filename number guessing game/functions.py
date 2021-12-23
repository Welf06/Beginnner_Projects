import random

players = {}

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
    
    num = random.randint(1,100)
    count= 0
    name = input("Enter your username: ").strip().lower()
    while True:
        try:
            guess= int(input('Enter your guess: '))
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
            print("You guessed correctly! \nIt took you", count, "turns to guess correctly")
            players[name] = players.get(name, 0) + count
            break

def leaderboard():
    """(None) -> None
    Prints the leaderboard
    """
    print ('name        guesses')
    for k in players:
        print (f'{k}            {players[k]}')
 
    