#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator")
input_price = float(input("Enter your bill ? "))
total_people = int(input("Enter no of friends? "))
tip_percent = int(input("Enter tip percentage? "))
per_person_amount = input_price / total_people
per_person_amount_with_tip = (per_person_amount * tip_percent)/100 + per_person_amount

print(f"Per person bill amount is {per_person_amount_with_tip:.2f}")

