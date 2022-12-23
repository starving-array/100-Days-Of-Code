# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
height_c = float(height)
weight_c = int(weight)

bmi = ( weight_c / ( height_c * height_c))
print(int(bmi))