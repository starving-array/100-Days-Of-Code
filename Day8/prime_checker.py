#Write your code below this line ๐
def prime_checker(number):
    prime = True

    for i in range(2, int(number**.5+1)):
        if(number%i==0):
            prime = False
            break
    if(prime== True):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
