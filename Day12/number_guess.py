#Number Guessing Game Objectives:
import random
from art import logo
def game_begin():
# Include an ASCII art logo.
  game_medium = input("Select game medium? 'Hard'/ 'Easy'=> ").lower()
  life_remain = 5
  if game_medium == 'easy':
    life_remain = 10
  print(f"Total guesses are {life_remain}. Best of luck")
    
  number_select = random.randrange(1,101)
  # Allow the player to submit a guess for a number between 1 and 100.
  while True:
    number_by_player = int(input("Guess for a number between 1 and 100=> "))
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    # If they got the answer correct, show the actual answer to the player.
    if number_by_player == number_select:
      print(f"You win! the answer is {number_select}")
      break
    elif number_by_player>number_select:
      life_remain -= 1
      print(f"Too high. Attempt left {life_remain}")
    else:
      life_remain -= 1
      print(f"Too low. Attempt left {life_remain}")
  
    if life_remain == 0:
      print("Game over")
      break

# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
while input("Do you want to play 'y'/'n' ").lower() == 'y':
    print(logo)
    game_begin()

