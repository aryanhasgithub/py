def pow(x,y):
    result =1
    while y>0:
        if y%2 == 0:
            x = x*x
            y >>=1
        else:
            result *= x
            y -=1
    return result
x= int(input("give x : "))
y = int(input("give y : "))

print("result: ", pow(x,y))
            