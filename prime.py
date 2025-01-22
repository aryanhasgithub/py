from math import sqrt
num1 = int(input("Enter a number: "))
if num1 > 1:
 for i in range(2, int(sqrt(num1)) + 1):
     if num1 % i == 0:
         print("Not a prime number")
         break
     else:
         print("Prime number")
         break
else:
    print("Not a prime number")     
     
    
    