

# add
def add(n1, n2):
  return n1 + n2

# sub 
def sub(n1, n2):
  return n1 - n2

# mul 
def mul(n1, n2):
  return n1 * n2

# div
def div(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}

from art_cal import logo
print(logo)

num1 = float(input("Please enter number: "))
ans = num1
while True:  
  for op in operations:
    print(op)
    
  option = input("Choose any operation to apply: ")

  num2 = float(input("Please enter another number: "))
  function = operations[option]
  # num1 = ans
  ans, num1 = function(ans, num2), ans
  print(f"{num1} {option} {num2} = {ans}")

  continues = input("Do you want to continue? y/n: ").lower()
  if continues == 'n':
    print("Bye Bye")
    break