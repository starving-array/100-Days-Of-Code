# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_year = int(age)
year = 90 - age_year
month = year * 12
week = year * 52
day = year * 365

print(f"You have {day} days, {week} weeks, and {month} months left.")