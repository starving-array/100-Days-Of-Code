alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def encrypt(text, shift):
  new_word = ''
  for i in text:
    if(alphabet.count(i)>0):  
      index = alphabet.index(i)
      new_index = (index+shift) % 26
      new_word += alphabet[new_index]
    else:
      new_word+=i
      
  print(f"Your encripted text is=> {new_word}")

def decrypt(text, shift):
  new_word = ''
  for i in text:
    if(alphabet.count(i)>0):  
      index = alphabet.index(i)
      new_index = (index-shift) % 26
      new_word += alphabet[new_index]
    else:
      new_word+=i
      
  print(f"Your decripted text is=> {new_word}")

while(True):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction== "encode":
    encrypt(text, shift)
  else:
    decrypt(text, shift)
  command = input("Do you want to exit y/n? ").lower()
  if(command=="y"):
    print("Good bye")
    break