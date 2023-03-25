import random
upper_bound =int(input("Enter the uper bound of the rage "))
lower_bound = int(input("Enter the lower bound of the range "))
num = int(input("Guess the number : "))
r=int(random.randrange(lower_bound,upper_bound))
if(num==r):
    print("your guess correct ")
elif(num>r):
    print("you are above the number!")
elif(num<r):
    print("you are below the number! ")
print("The random number is:"+str(r))
