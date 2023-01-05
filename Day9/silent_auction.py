from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Welcome to silent auction")

silent_auc_database = []

def add_data_to_auc(name, price):
  database = {}
  database['name'] = name
  database['price'] = price
  silent_auc_database.append(database)

def check_winner():
  max_index = 0
  for key in range(len(silent_auc_database)):
    if(silent_auc_database[key]['price']>silent_auc_database[max_index]['price']):
      max_index = key
      
  print(f"The winner of the auction is=> {silent_auc_database[max_index]['name']}.")


while(True):
  name = input("Enter your name? ")
  price = int(input("Enter your bid? "))
  add_data_to_auc(name, price)

  status = input("Do you want to add more bidding? y/n ").lower()
  clear()
  if(status == 'n'):
    check_winner()
    print("============================")
    print("Thank you for using silent auction")
    break
