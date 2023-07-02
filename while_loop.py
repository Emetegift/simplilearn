# i = 1  ## Where i is a counter
# while i <=10:
#     print('simplilearn')
#     i+=1 ## this will increment the value of i

# i = 10  ## Where i is a counter
# while i >=1:
#     print('simplilearn')
# #     i-=1 ## this will decrease the value of i from 10 to 1

# ## To find sum of the first natural numbers
# i=1
# sum=0
# while i<=10:
#     sum = sum+i
#     i+=1
# print(sum)
    


# ## To find sum of even numbers
# i=1
# sum=0
# while i<=10:
#     if i%2==0:
#         sum = sum+i
#     i+=1
# print(sum)

# ## To reverse an integer by taking input from the users
# n= int(input("Eneter a number "))
# nr = 0 ## where nr is a reversal of n
# while n%10!=0:
#     c=n%10
#     nr=nr*10 + c
#     n=n//10
# print(nr)   

## A simple guessing game using a while loop
import random

nump = random.randint(1000, 9999)
n = int(input("Enter a number"))
while n%10!=0:
    num = nump
    cor =0
    while num%10!=0:
        numc = num%10
        nc = n%10
        num = num//10
        n = n//10
        if numc==nc:
            cor+=1
    if cor==4:
        print("Congrats! you guesses it right")
        break
    else:
        print("%d digits were guessed correctly" %cor)
        ## To give the user another chance to try and guess again
        n =int(input("Enter a number"))
else:
    print("You quit the game ")
        
        






    



