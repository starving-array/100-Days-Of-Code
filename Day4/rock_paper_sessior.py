# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
'''
rules
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''
modes = ['rock', 'scissor', 'paper']
mode_view = [rock, scissors, paper]

print("Welcome to rock paper scissor game")

while(True):
    pc_select_mode = random.randint(0,2)
    user_select_input = input("Enter your choice: Rock | Paper | Scissor ").lower()

    print(f"PC selects: {modes[pc_select_mode]}")
    print(mode_view[pc_select_mode])

    print(f"You have selected {user_select_input}")
    print(mode_view[modes.index(user_select_input)])

    if(modes[pc_select_mode] ==  user_select_input):
        print("Match draw. Select again")
        continue
    if(modes[pc_select_mode] == 'rock' and user_select_input != 'paper'):
        print("You lost, PC won")
    elif(modes[pc_select_mode] == 'scissor' and user_select_input == 'paper'):
        print("You lost, PC won")
    elif(modes[pc_select_mode] == 'paper' and user_select_input == 'rock'):
        print("You lost, PC won")
    else:
        print("You won.")
    break;



