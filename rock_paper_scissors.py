import random

print('     ROCK, PAPER and SCISSORS')

count = 1
choice = ['rock', 'paper', 'scissor']
win = 0
lose= 0 
while count<6:
    print(f'ROUND {count}')
    user = input('Enter your choice: ').lower().strip()
    comp = random.choice(choice)
    if user not in choice:
        count -= 1
        print('Please select one from: rock, paper and scissors')
    else:
        print(f"Computer's choice: {comp}")
    if comp == user:
        print(f'Tie! Both of you chose {comp}')
    elif user == 'rock' :
        if comp == 'paper':
            print('You lose :C')
            lose += 1
        if comp == 'scissor':
            print('you win :D')
            win += 1
    elif user == 'paper' : 
        if comp == 'scissor':
            print('You lose :C')
            lose += 1
        if comp == 'rock':
            print('you win :D')
            win += 1
    elif user == 'scissor' :
        if comp == 'rock':
            print('You lose :C')
            lose += 1
        if comp == 'paper':
            print('you win :D')
            win += 1
    count += 1
print(f"You won {win} times\n Computer won {lose} times ")
if win > lose:
    print('You win! Congratulations')
elif lose > win:
    print('You lose! Better luck next time')
else:
    print('Tie!')