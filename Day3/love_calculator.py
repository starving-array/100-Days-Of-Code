# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

name_couple = name1_lower + name2_lower

t_count = 0
l_count = 0

t_count += name_couple.count("t") + name_couple.count("r") + name_couple.count("u") + name_couple.count("e")

l_count += name_couple.count("l") + name_couple.count("o") + name_couple.count("v") + name_couple.count("e")

love_percent = int(str(t_count) + str(l_count))

if(love_percent < 10 or love_percent > 90):
    print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif(love_percent> 40 and love_percent<50):
    print(f"Your score is {love_percent}, you are alright together.")
else:
    print(f"Your score is {love_percent}.")

