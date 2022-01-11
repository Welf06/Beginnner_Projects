from random import randint
# 0: draw 1:lost 2:won
matrix = [[0,1,2],
          [2,0,1],
          [1,2,0]]
choices = ["rock", "paper", "scissors"]
choice_map = {"rock": 0, "paper":1, "scissors":2}
comp_choice = randint(0,2)
user_choice = input("Please choose rock, paper or scissors:\n").lower().strip()
user_choice = choice_map.get(user_choice)
outcome = matrix[user_choice][comp_choice]
outcomes = ["Tie", "You lost", "You won"]
print(f"Compter's choice: {choices[comp_choice]}")
print(outcomes[outcome])


