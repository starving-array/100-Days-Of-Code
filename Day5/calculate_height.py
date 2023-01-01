
print("Enter heights with space in between! i.e => 178 190 110")
height_input = input("=> ")

height_split = height_input.split(" ");

count = 0
total = 0;

for h in height_split:
    count+=1
    total += int(h)

avg_height =round( total/count )

print(f"Avg height is=> {avg_height}")