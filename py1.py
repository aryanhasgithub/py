num=20
for i in range(1,11):
    mul=i*num
    print(f"20 x {i}={mul}")
    
    #star pattern
stano=int(input("input no of rows"))
for i in range(0,stano):    
    for c in range(0,i+1):
        print("*", end=" ")
    print("\n")

#sum of first ten natural no
num=1
sum=0
while (num<=10):
    sum=sum+num
    num=num+1

print("sum of ten natural no is",sum)   

#this prime or not
primeno=int(input("input a number to check if it is prime"))
booleanval=False
if primeno>1:
    for i in range(2,primeno):
        if (primeno%i==0):
            booleanval=True
            break
if booleanval:
    print("this is not a prime no") 
else:
    print("it is prime")



            










