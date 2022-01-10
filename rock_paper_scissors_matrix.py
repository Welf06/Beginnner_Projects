from random import choice
# 0: draw 1:lost 2:won
matrix = [[0,1,2],
          [2,0,1],
          [1,2,0]]
choices = ["rock", "paper", "scissors"]
choice_map = {"rock": 0, "paper":1, "scissors":2}
comp_choice = choice(choices)
user_choice = input("Please choose rock, paper or scissors:\n").lower().strip()
comp_choice = choice_map.get(comp_choice)
user_choice = choice_map.get(user_choice)
outcome = matrix[user_choice][comp_choice]
outcomes = ["Tie", "You lost", "You won"]
print(outcomes[outcome])


