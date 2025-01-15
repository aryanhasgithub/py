number = int(input("Enter number to be checked: "))
result = 0
temp = number
while temp !=0:
    digit = temp % 10 
    result = result + digit**3
    temp = temp // 10
print(result)
if number == result:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")    
        
    
    