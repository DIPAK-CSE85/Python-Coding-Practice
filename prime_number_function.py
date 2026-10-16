def prime(num):
    is_prime=True
    if num==1:
        is_prime=False
    for i in range(2,num):    
        if num%2==0:
            is_prime=False
    if(is_prime==True):
        print("the given numner is prime")   
    else:
        print("the given number is not prime")     
num=int(input("enter a any number="))     
prime(num)   


# my making range half using ceil function
import math
def prime(num):
    is_prime=True
    if num==1:
        is_prime=False
    for i in range(2,math.ceil(num/2)+1):    
        if num%2==0:
            is_prime=False
    if(is_prime==True):
        print("the given numner is prime")   
    else:
        print("the given number is not prime")     
num=int(input("enter a any number="))     
prime(num)   

          
        