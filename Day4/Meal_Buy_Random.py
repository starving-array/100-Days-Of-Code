# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_person_count = len(names)
person_index_select = random.randint(0, total_person_count-1)

person_name = names[person_index_select]

print(f"{person_name} is going to buy the meal today!")

